import logging

from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import DateTimeField, Model, Manager, DO_NOTHING, QuerySet
from django.db.models.fields.related import OneToOneField, ManyToManyField, ManyToManyRel, ForeignKey
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from SmartERP.middlewares.users import get_current_user_id, get_signed_in_user

LOGGER = logging.getLogger(__name__)


def _unset_related_one_to_one(obj, field):
    old_value = getattr(obj, field.column)
    if old_value is not None:
        LOGGER.debug(
            'Setting %s.%s to None on object %s (old value: %s)',
            obj._meta.model.__name__, field.column, obj.pk, old_value)
        # Unset the fk field (e.g. Foo.baz_id)
        setattr(obj, field.column, None)
        # Unset the related object field (e.g. Foo.baz)
        setattr(obj, field.name, None)


def _unset_related_many_to_many(obj, field):
    manager = getattr(obj, field.name)
    old_values = manager.values_list('pk', flat=True)
    LOGGER.debug(
        'Removing all objects from %s.%s on object %s (old values: %s)',
        obj._meta.model.__name__, field.name, obj.pk,
        ', '.join(str(pk) for pk in old_values))
    manager.remove(*manager.all())


def _unset_related_objects_relations(obj):
    LOGGER.debug('Soft-deleting object %s %s',
                 obj._meta.model.__name__, obj.pk)

    if hasattr(obj._meta, 'get_fields'):
        for field in obj._meta.get_fields():
            field_type = type(field)

            if field_type is OneToOneField:
                _unset_related_one_to_one(obj, field)
            elif field_type in (ManyToManyRel, ManyToManyField):
                _unset_related_many_to_many(obj, field)

    for related in obj._meta.get_all_related_objects():
        # Unset related objects' relation
        rel_name = related.get_accessor_name()

        if related.one_to_one:
            # Handle one-to-one relations.
            try:
                related_object = getattr(obj, rel_name)
            except ObjectDoesNotExist:
                pass
            else:
                _unset_related_one_to_one(related_object, related.field)
                related_object.save()

        else:
            # Handle one-to-many and many-to-many relations.
            related_objects = getattr(obj, rel_name)
            if related_objects.count():
                affected_objects_id = ', '.join(
                    str(pk) for pk in related_objects.values_list(
                        'pk', flat=True))
                old_values = ', '.join(
                    str(val) for val in related_objects.values_list(
                        related.field.name, flat=True))
                LOGGER.debug(
                    'Setting %s.%s to None on objects %s (old values: %s)',
                    related_objects.model.__name__, related.field.name,
                    affected_objects_id, old_values)
                related_objects.update(**{related.field.name: None})


class SoftDeleteQuerySet(QuerySet):
    """
    This QuerySet subclass implements soft deletion of objects.
    """

    def delete(self):
        """
        Soft delete all objects included in this queryset.
        """
        # for obj in self:
        #     _unset_related_objects_relations(obj)

        self.update(deleted_time=now())

    def undelete(self):
        """
        Soft undelete all objects included in this queryset.
        """
        objects = self.filter(deleted_time__isnull=False)
        if objects.count():
            LOGGER.debug(
                'Soft undeleting %s objects: %s', self.model.__name__,
                ', '.join(str(pk)
                          for pk in objects.values_list('pk', flat=True)))
            objects.update(deleted_time=None)


class SoftDeleteQuerySet2(QuerySet):
    """
    This QuerySet subclass implements soft deletion of objects.
    """

    def delete(self):
        """
        Soft delete all objects included in this queryset.
        """
        # for obj in self:
        #     _unset_related_objects_relations(obj)

        self.update(deleted_time=now())

    def undelete(self):
        """
        Soft undelete all objects included in this queryset.
        """
        objects = self.filter(deleted_time__isnull=False)
        if objects.count():
            LOGGER.debug(
                'Soft undeleting %s objects: %s', self.model.__name__,
                ', '.join(str(pk)
                          for pk in objects.values_list('pk', flat=True)))
            objects.update(deleted_time=None)


class SoftDeleteManager(Manager.from_queryset(SoftDeleteQuerySet)):
    """
    This Manager hides soft deleted objects by default,
    and exposes methods to access them.
    """

    def _get_base_queryset(self):
        return super(SoftDeleteManager, self).get_queryset()

    def get_queryset(self):
        """
        Return NOT DELETED objects.
        """
        return self._get_base_queryset().filter(deleted_time__isnull=True)

    def deleted(self):
        """
        Return DELETED objects.
        """
        return self._get_base_queryset().filter(deleted_time__isnull=False)

    def with_deleted(self):
        """
        Return ALL objects.
        """
        return self._get_base_queryset()


class ModelByCompanyManager(SoftDeleteManager):
    def get_queryset(self):
        """
        Return NOT DELETED objects.
        """
        q = self._get_base_queryset()
        # if get_current_company_id():
        #     q = q.filter(company_id=get_current_company_id())
        return q.filter(deleted_time__isnull=True)


class AllManager(Manager.from_queryset(SoftDeleteQuerySet2)):
    """
    This Manager hides soft deleted objects by default,
    and exposes methods to access them.
    """

    def get_queryset(self):
        """
        Return NOT DELETED objects.
        """
        return super(AllManager, self).get_queryset()


class BaseModel(Model):
    """
    Simply inherit this class to enable soft deletion on a model.
    """

    class Meta:
        abstract = True

    objects = SoftDeleteManager()
    all_objects = AllManager()
    deleted_time = DateTimeField(verbose_name=_('deleted_time'), null=True, blank=True)
    created_date = DateTimeField(auto_now_add=True, null=True)
    modified_date = DateTimeField(auto_now=True, null=True)
    created_by = ForeignKey("erp_user.User", on_delete=DO_NOTHING, null=True, related_name="+")
    modified_by = ForeignKey("erp_user.User", on_delete=DO_NOTHING, null=True, related_name="+")
    deleted_by = ForeignKey("erp_user.User", on_delete=DO_NOTHING, null=True, related_name="+")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.before_save()
        self.is_new = not self.id
        self.created_by = self.created_by if self.created_by else get_signed_in_user()
        self.modified_by = get_signed_in_user()
        super().save(force_insert, force_update, using, update_fields)
        self.after_save()
        return self

    def delete(self, *args, **kwargs):
        """
        Soft delete this object.
        """
        # _unset_related_objects_relations(self)
        self.before_delete()
        self.deleted_time = now()
        self.deleted_by_id = get_current_user_id()
        super().save()
        self.after_delete()

        return self

    def undelete(self):
        """
        Undelete this soft-deleted object.
        """
        if self.deleted_time is not None:
            LOGGER.debug('Soft-undeleting object %s %s',
                         self._meta.model.__name__, self.pk)
            self.deleted_time = None
            self.save()

        return self

    def before_save(self):
        pass
        # if hasattr(self, 'company') and getattr(self, 'company') is None and getattr(self, 'company_id', None) is None:
        #     self.company_id = get_current_company_id()

    def after_save(self):
        pass

    def before_delete(self):
        pass

    def after_delete(self):
        pass

    def dict(self):
        return {"id": self.id, "name": str(self)}


# class ModelByCompany(BaseModel):
#     def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
#         if not self.company_id:
#             self.company_id = get_current_company_id()
#         return super().save(force_insert, force_update, using, update_fields)
#
#     objects = ModelByCompanyManager()
#     company = ForeignKey("company.CompanyModel", null=True, related_name="+", on_delete=DO_NOTHING)
#
#     class Meta:
#         abstract = True


class ModelAdmin(admin.ModelAdmin):
    exclude = ('deleted_time',)

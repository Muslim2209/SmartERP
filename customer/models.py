from django.db import models

from category.models import Category


class CustomerGroup(Category):
    pass


class Customer(models.Model):
    name = models.CharField(max_length=640)
    short_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField('erp_user.User', on_delete=models.PROTECT, null=True, related_name='customer')
    group = models.CharField(max_length=960, null=True, blank=True)
    info = models.OneToOneField('document.Info', on_delete=models.PROTECT, null=True, blank=True,
                                related_name='owner_customer')
    document = models.OneToOneField('document.Document', on_delete=models.PROTECT, null=True, blank=True,
                                    related_name='owner_customer')
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.user.get_full_name() if self.user else ""}'

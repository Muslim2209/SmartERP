from django.utils.translation import ugettext_lazy as _


class CONSTANTS:
    class COMPANY:
        class STATUS:
            ACTIVE = "ACTIVE"
            INACTIVE = "INACTIVE"
            DEFAULT = ACTIVE
            CHOICES = (
                (ACTIVE, _('Active')),
                (INACTIVE, _('Inactive')),
            )
            AS_RESPONSE = {
                'choices': [{"name": y, "code": x} for x, y in CHOICES],
                'default': DEFAULT
            }

    class USER:
        class GENDER:
            MALE = 'MALE'
            FEMALE = 'FEMALE'
            DEFAULT = MALE
            CHOICES = (
                (MALE, _('Male')),
                (FEMALE, _('Female')),
            )
            AS_RESPONSE = {
                'choices': [{"name": y, "code": x} for x, y in CHOICES],
                'default': DEFAULT
            }

        class ROLES:
            USER = 'USER'
            WAREHOUSE_KEEPER = 'WAREHOUSE_KEEPER'
            DEFAULT = USER
            CHOICES = (
                (USER, _('User')),
                (WAREHOUSE_KEEPER, _('Warehouse keeper')),
            )
            AS_RESPONSE = {
                'choices': [{"name": y, "code": x} for x, y in CHOICES],
                'default': DEFAULT
            }

    class LANGUAGE:
        UZBEK = 'UZBEK'
        ENGLISH = 'ENGLISH'
        RUSSIAN = 'RUSSIAN'
        DEFAULT = UZBEK
        CHOICES = (
            (UZBEK, _("O'zbek")),
            (ENGLISH, _('English')),
            (RUSSIAN, _('Русский язык')),
        )
        AS_RESPONSE = {
            'choices': [{"name": y, "code": x} for x, y in CHOICES],
            'default': DEFAULT
        }

    class ORDER:
        class STATUS:
            NEW = 'NEW'
            DRAFT = 'DRAFT'
            IN_PROGRESS = 'IN_PROGRESS'
            WAITING = 'WAITING'
            SHIPPED = 'SHIPPED'
            DELIVERED = 'DELIVERED'
            ARCHIVE = 'ARCHIVE'
            DEFAULT = NEW
            CHOICES = (
                (NEW, _('New')),
                (DRAFT, _('Draft')),
                (IN_PROGRESS, _('In progress')),
                (WAITING, _('Waiting')),
                (SHIPPED, _('Shipped')),
                (DELIVERED, _('Delivered')),
                (ARCHIVE, _('Archive')),
            )
            AS_RESPONSE = {
                'choices': [{"name": y, "code": x} for x, y in CHOICES],
                'default': DEFAULT
            }

    class WAREHOUSE:
        class INPUT_STATUS:
            DRAFT = 'DRAFT'
            ACCEPTED = 'ACCEPTED'
            CHOICES = (
                (DRAFT, _('Draft')),
                (ACCEPTED, _('Accepted')),
            )

    class PRODUCT:
        class TRANSACTION:
            class TYPE:
                SOLD = 'SOLD'
                BOOKED = 'BOOKED'
                NEW = 'NEW'
                ARRIVED = 'ARRIVED'

                CHOICES = (
                    (SOLD, _('Sold')),
                    (BOOKED, _('Booked')),
                    (NEW, _('New')),
                    (ARRIVED, _('Arrived')),
                )

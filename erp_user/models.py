from django.contrib.auth.models import AbstractUser
from django.db import models
from tools.config import CONSTANTS


class User(AbstractUser):
    phone_number = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, default=CONSTANTS.USER.GENDER.DEFAULT,
                              choices=CONSTANTS.USER.GENDER.CHOICES)
    language = models.CharField(max_length=12, default=CONSTANTS.LANGUAGE.DEFAULT, choices=CONSTANTS.LANGUAGE.CHOICES)
    role = models.CharField(max_length=96, choices=CONSTANTS.USER.ROLES.CHOICES, null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='team')
    info = models.OneToOneField('document.Info', on_delete=models.PROTECT, null=True, blank=True,
                                related_name='owner_user')
    document = models.OneToOneField('document.Document', on_delete=models.PROTECT, null=True, blank=True,
                                    related_name='owner_user')

from django.db import models
from tools.config import CONSTANTS


class Company(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=96, choices=CONSTANTS.COMPANY.STATUS.CHOICES)
    info = models.OneToOneField('document.Info', on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey('company.Company', on_delete=models.PROTECT, related_name='branches')
    user = models.ForeignKey('erp_user.User', on_delete=models.PROTECT)
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT, null=True, blank=True)
    info = models.OneToOneField('document.Info', on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'branches'

    def __str__(self):
        return self.name

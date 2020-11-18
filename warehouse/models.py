from django.db import models
from django.utils import timezone

from tools.config import CONSTANTS


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    accountable = models.ForeignKey('erp_user.User', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class WarehouseInput(models.Model):
    number = models.IntegerField()
    warehouse = models.ForeignKey('Warehouse', on_delete=models.PROTECT, related_name='inputs')
    vendor = models.ForeignKey('reference.Vendor', on_delete=models.PROTECT, related_name='inputs', null=True,
                               blank=True)
    note = models.CharField(max_length=640, null=True, blank=True)
    input_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=64, choices=CONSTANTS.WAREHOUSE.INPUT_STATUS.CHOICES)

    def __str__(self):
        return f'№{self.number}'


class InputProduct(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, related_name='inputs')
    quantity = models.IntegerField()
    price = models.FloatField()
    expire_date = models.DateField(null=True, blank=True)
    wh_input = models.ForeignKey('WarehouseInput', on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return f'{self.product.name} - {self.quantity} - {self.wh_input.warehouse.name}'


class Remain(models.Model):
    amount = models.IntegerField()
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, related_name='remains')
    warehouse = models.ForeignKey('Warehouse', on_delete=models.PROTECT, related_name='remains')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.amount}pcs in {self.warehouse.name}'

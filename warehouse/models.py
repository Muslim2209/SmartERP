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
    price = models.DecimalField(decimal_places=4, max_digits=16)
    expire_date = models.DateField(null=True, blank=True)
    wh_input = models.ForeignKey('WarehouseInput', on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return f'{self.product.name} - {self.quantity} - {self.wh_input.warehouse.name}'


class ProductOut(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, related_name='outs')
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=4, max_digits=16)
    order = models.ForeignKey('order.OrderItem', on_delete=models.PROTECT, related_name='outs')

    def __str__(self):
        return f'{self.product.name} - {self.order.amount} - {self.order.price}'


class Balance(models.Model):
    # amount = models.IntegerField()
    # product = models.ForeignKey('product.Product', on_delete=models.PROTECT, related_name='remains')
    # warehouse = models.ForeignKey('Warehouse', on_delete=models.PROTECT, related_name='remains')
    income = models.ForeignKey('InputProduct', on_delete=models.PROTECT, null=True, blank=True)
    outgo = models.ForeignKey('ProductOut', on_delete=models.PROTECT, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.income} - {self.outgo}'

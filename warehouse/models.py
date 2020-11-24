from django.db import models
from django.db.models import F
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


class Stock(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=4, max_digits=20)
    expire_date = models.DateField(null=True, blank=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.PROTECT, related_name='stocks')
    transaction = models.ForeignKey('ProductTransaction', on_delete=models.CASCADE, related_name='stocks')
    timestamp = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def increase_stock(self, quantity: int, commit: bool = True):
        self.quantity = F("quantity") + quantity
        if commit:
            self.save(update_fields=["quantity"])

    def decrease_stock(self, quantity: int, commit: bool = True):
        self.quantity = F("quantity") - quantity
        if commit:
            self.save(update_fields=["quantity"])

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'


class ProductTransaction(models.Model):
    number = models.PositiveIntegerField(null=True, blank=True)
    transaction_type = models.CharField(max_length=255, choices=CONSTANTS.PRODUCT.TRANSACTION.TYPE.CHOICES)
    note = models.CharField(max_length=640, null=True, blank=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.PROTECT, related_name='transactions')
    timestamp = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        pk = self.pk
        super().save(*args, **kwargs)
        # print('pk\n', pk)
        # print('instance\n', self.__dict__)
        if self.transaction_type in ['NEW', 'ARRIVED']:
            for item in self.items.all():
                # print('item\n', item.__dict__)
                self.stocks.create(product=item.product, quantity=item.quantity,
                                   price=item.price, warehouse=self.warehouse)


class TransactionItem(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='transactions')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=4, max_digits=20)
    transaction = models.ForeignKey('ProductTransaction', on_delete=models.CASCADE, related_name='items')

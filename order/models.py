from django.db import models
from django.utils import timezone

from tools.config import CONSTANTS


class OrderItem(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT)
    price = models.ForeignKey('price.ProductPrice', on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    order = models.ForeignKey('order.Order', on_delete=models.PROTECT, related_name='items')

    @property
    def total_sum(self):
        return self.price.amount * self.amount

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey('erp_user.User', on_delete=models.PROTECT, related_name='orders')
    customer = models.ForeignKey('customer.Customer', on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=255, choices=CONSTANTS.ORDER.STATUS.CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    deliver_date = models.DateTimeField(default=timezone.now)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.customer} - {self.total_sum}'

    @property
    def total_sum(self):
        return sum(item.total_sum for item in self.items.all())

from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.name


class Price(models.Model):
    name = models.CharField(max_length=255)
    currency = models.ForeignKey('price.Currency', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    price = models.ForeignKey('price.Price', on_delete=models.PROTECT)
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, related_name='prices')
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.price.name} - {self.amount}'

from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=255)
    decimal_name = models.CharField(max_length=255, null=True, blank=True)
    fraction_name = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=255, null=True, blank=True)
    prefix = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    suffix = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=6)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.name


class Price(models.Model):
    code = models.CharField(max_length=6, null=True, blank=True)
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey('price.Currency', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    price = models.ForeignKey('price.Price', on_delete=models.PROTECT)
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, related_name='prices')
    amount = models.DecimalField(decimal_places=4, max_digits=16)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.name} - {self.price.name} - {self.amount}'

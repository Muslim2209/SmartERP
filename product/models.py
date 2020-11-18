from django.db import models

from category.models import Category, SubCategory


class ProductGroup(Category):
    pass


class ProductSubGroup(SubCategory):
    group = models.ForeignKey('ProductGroup', on_delete=models.PROTECT, related_name='subtypes')


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    weight_brutto = models.FloatField(null=True, blank=True)
    weight_netto = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    group = models.CharField(max_length=960, null=True, blank=True)
    manufacturer = models.ForeignKey('reference.Manufacturer', on_delete=models.PROTECT, related_name='products',
                                     null=True, blank=True)
    country = models.ForeignKey('reference.Country', on_delete=models.PROTECT, related_name='products', null=True,
                                blank=True)
    measure = models.ForeignKey('unit.Unit', on_delete=models.PROTECT, related_name='products')
    box_type = models.ForeignKey('unit.Case', on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    box_quantity = models.IntegerField(null=True, blank=True)
    order_number = models.IntegerField(null=True, blank=True)
    document = models.OneToOneField('document.Document', on_delete=models.PROTECT, null=True, blank=True)
    product_tares = models.ManyToManyField('self', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

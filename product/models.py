from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    qr_code = models.CharField(max_length=255, null=True, blank=True)
    netto = models.FloatField(null=True, blank=True)
    brutto = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    category = models.ForeignKey('category.Category', on_delete=models.PROTECT, related_name='products')
    group = models.ForeignKey('category.Group', on_delete=models.PROTECT, related_name='products', null=True,
                              blank=True)
    manufacturer = models.ForeignKey('reference.Manufacturer', on_delete=models.PROTECT, related_name='products',
                                     null=True, blank=True)
    country = models.ForeignKey('reference.Country', on_delete=models.PROTECT, related_name='products', null=True,
                                blank=True)
    measure = models.ForeignKey('unit.Unit', on_delete=models.PROTECT, related_name='products')
    case_type = models.ForeignKey('unit.Case', on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    box_quantity = models.IntegerField(null=True, blank=True)
    document = models.OneToOneField('document.Document', on_delete=models.PROTECT, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

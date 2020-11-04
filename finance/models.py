from django.db import models


class CashBox(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey('price.Currency', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'cashboxes'

    def __str__(self):
        return self.name

from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    accountable = models.ForeignKey('erp_user.User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


# class WarehouseInput(models.Model):
#     amount = models.IntegerField()
#     product = models.ManyToManyField('product.Product')
#     warehouse = models.ForeignKey('warehouse.Warehouse', on_delete=models.PROTECT, related_name='warehouse_remains')
#     timestamp = models.DateTimeField(auto_now_add=True)


class Remain(models.Model):
    amount = models.IntegerField(default=0)
    product = models.ForeignKey('product.Product', on_delete=models.PROTECT, related_name='product_remains')
    warehouse = models.ForeignKey('warehouse.Warehouse', on_delete=models.PROTECT, related_name='warehouse_remains')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.amount}pcs in {self.warehouse.name}'

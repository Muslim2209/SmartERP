from django.contrib import admin

from warehouse.models import *

admin.site.register(Warehouse)
admin.site.register(Stock)
admin.site.register(ProductTransaction)
admin.site.register(TransactionItem)

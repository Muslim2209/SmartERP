from django.contrib import admin

from warehouse.models import Warehouse, Remain, InputProduct, WarehouseInput

admin.site.register(Warehouse)
admin.site.register(Remain)
admin.site.register(InputProduct)


class InputProductInline(admin.TabularInline):
    model = InputProduct


@admin.register(WarehouseInput)
class WarehouseInputAdmin(admin.ModelAdmin):
    list_display = ['number', 'warehouse', 'created_date', 'status']
    inlines = [InputProductInline]

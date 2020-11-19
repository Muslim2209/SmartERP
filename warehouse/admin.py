from django.contrib import admin

from warehouse.models import Warehouse, Balance, InputProduct, WarehouseInput

admin.site.register(Warehouse)
admin.site.register(Balance)
admin.site.register(InputProduct)


class InputProductInline(admin.TabularInline):
    model = InputProduct


@admin.register(WarehouseInput)
class WarehouseInputAdmin(admin.ModelAdmin):
    list_display = ['number', 'warehouse', 'created_date', 'status']
    list_display_links = ['number', 'warehouse']
    inlines = [InputProductInline]

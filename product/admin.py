from django.contrib import admin

from price.models import ProductPrice
from product.models import Product


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPriceInline]

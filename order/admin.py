from django.contrib import admin

from order.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'user', 'total_sum', 'created_date', 'deliver_date']
    inlines = [OrderItemInline]

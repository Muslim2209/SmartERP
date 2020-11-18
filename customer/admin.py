from django.contrib import admin

from customer.models import Customer, CustomerGroup

admin.site.register(Customer)
admin.site.register(CustomerGroup)

from django.contrib import admin

from price.models import Price, Currency, ProductPrice

admin.site.register(Price)
admin.site.register(ProductPrice)
admin.site.register(Currency)

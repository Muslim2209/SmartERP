from django.contrib import admin

from reference.models import Country, Region, City, Manufacturer, Brand, Vendor

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(Vendor)

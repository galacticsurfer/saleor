from django.contrib import admin
from .models import ShippingMethod, ShippingMethodCountry

admin.site.register(ShippingMethod)
admin.site.register(ShippingMethodCountry)
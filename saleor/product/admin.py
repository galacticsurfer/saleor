from django.contrib import admin
from django.db.models import Sum
from mptt.admin import MPTTModelAdmin

from ..discount.models import Sale
from .models import (ProductImage, Category, Product, ProductAttribute, ProductVariant, Stock, AttributeChoiceValue,
                     ProductClass)
#from .forms import ImageInline

#
# class ImageAdminInline(admin.StackedInline):
#     model = ProductImage
#     formset = ImageInline


class ProductCollectionAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    model = Product
    #inlines = [ImageAdminInline, ]


class ProductVariantAdmin(admin.ModelAdmin):
    model = ProductVariant
    list_display = ['name', 'get_inventory']

    def get_inventory(self, obj):
        return obj.inventory.all().aggregate(Sum('quantity'))['quantity__sum']
    get_inventory.short_description = 'Inventory'


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute)
admin.site.register(ProductVariant, ProductVariantAdmin)
admin.site.register(Stock)
admin.site.register(AttributeChoiceValue)
admin.site.register(Sale)
admin.site.register(ProductClass)

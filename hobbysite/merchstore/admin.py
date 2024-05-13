from django.contrib import admin
from .models import Product, ProductType


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type',  'product_type_description', 'description', 'formatted_price')
    search_fields = ['name']

    def formatted_price(self, obj):
        return '₱%.2f' % obj.price
    formatted_price.short_description = 'Price'

    def product_type_description(self, obj):
        return obj.product_type.description
    product_type_description.short_description = 'Product Type Description'

    def get_absolute_url(self, obj):
        return obj.get_absolute_url()


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

    def get_absolute_url(self, obj):
        return obj.get_absolute_url()

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
from django.contrib import admin
from .models import Product, ProductBasePhoto

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['product_number', 'product_specification', 'product_category', 'product_technical_data', 'unit_price', 'short_text']
    list_display = ('product_number', 'product_specification', 'product_category', 'product_technical_data', 'unit_price', 'short_text')
    search_fields = ['product_number', 'product_specification']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBasePhoto)

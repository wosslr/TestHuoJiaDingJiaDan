from django.contrib import admin
from .models import Product, ProductBasePhoto, ProductStyle

# Register your models here.


class ProductBasePhotoInline(admin.TabularInline):
    model = ProductBasePhoto
    extra = 0
    verbose_name_plural = verbose_name = '产品底图'

class ProductStyleInline(admin.TabularInline):
    model = ProductStyle
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    fields = ['product_number', 'product_specification', 'product_category', 'product_technical_data', 'unit_price', 'short_text']
    inlines = [ProductBasePhotoInline, ProductStyleInline]
    list_display = ('product_number', 'product_specification', 'product_category', 'product_technical_data', 'unit_price', 'short_text')
    search_fields = ['product_number', 'product_specification']

admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductBasePhoto)

from django.contrib import admin
from .models import Product, ProductBasePhoto, ProductStyle, ProductPresetStyle, ProductStyleItem

# Register your models here.


class ProductBasePhotoInline(admin.TabularInline):
    model = ProductBasePhoto
    extra = 0
    verbose_name_plural = verbose_name = '产品底图'


class ProductStyleInline(admin.TabularInline):
    model = ProductStyle
    extra = 0


class ProductStyleItemInline(admin.TabularInline):
    model = ProductStyleItem
    extra = 0
    # template = 'custom_admin/edit_inline/tabular.html'

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'base_photo':
            product_style_id = request.path.split('/')[-2]
            try:
                product_style = ProductStyle.objects.filter(id=product_style_id)[0]
                kwargs['queryset'] = ProductBasePhoto.objects.filter(product_id=product_style.product.id)
            except Exception as e:
                print(e)
                pass

        return super(ProductStyleItemInline, self).formfield_for_foreignkey(db_field, request, **kwargs)


class ProductPresetStyleInline(admin.TabularInline):
    model = ProductPresetStyle
    extra = 0


class ProductStyleAdmin(admin.ModelAdmin):
    list_display = ['product', 'style_name', 'style_part_name']
    list_display_links = ['style_name']
    inlines = [ProductStyleItemInline]


class ProductAdmin(admin.ModelAdmin):
    fields = ['product_number', 'product_specification', 'product_category', 'product_technical_data', 'unit_price', 'short_text']
    inlines = [ProductBasePhotoInline, ProductStyleInline, ProductPresetStyleInline]
    list_display = ('product_number', 'product_specification', 'product_category', 'product_technical_data', 'unit_price', 'short_text')
    search_fields = ['product_number', 'product_specification']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductStyle, ProductStyleAdmin)
# admin.site.register(ProductBasePhoto)

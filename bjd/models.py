# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    product_number = models.CharField(max_length=150, verbose_name='型号')    #型号
    product_specification = models.CharField(max_length=100, verbose_name='规格')  #规格
    product_category = models.CharField(max_length=100, verbose_name='类型')  #类型
    product_technical_data = models.CharField(max_length=250, blank=True, verbose_name='技术参数')  #技术参数
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='单价')  #单价
    short_text = models.TextField(max_length=500, blank=True, verbose_name='备注')  #备注

    def __str__(self):
        return self.product_number

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'


class ProductBasePhoto(models.Model):
    product = models.ForeignKey(Product, verbose_name='产品')
    photo_name = models.CharField(max_length=50, verbose_name='图片描述')
    photo_data = models.ImageField(upload_to='base_photo', verbose_name='底图')

    def __str__(self):
        return self.photo_name

    class Meta:
        verbose_name_plural = verbose_name = '产品底图'
        unique_together = ('product', 'photo_name')


class ProductStyle(models.Model):
    product = models.ForeignKey(Product, verbose_name='产品')
    # product_base_photo = models.ForeignKey(ProductBasePhoto, verbose_name='产品底图')
    style_part_name = models.CharField(max_length=50, verbose_name='变色部分')
    style_name = models.CharField(max_length=50, verbose_name='样式颜色')
    style_color_code = models.CharField(max_length=100, verbose_name='颜色代码')

    def __str__(self):
        return self.style_name

    class Meta:
        verbose_name_plural = verbose_name = '产品样式'


class ProductStyleItem(models.Model):
    product_style = models.ForeignKey(ProductStyle, verbose_name='产品样式')
    # base_photo_name = models.CharField(max_length=50, verbose_name='图片描述')
    base_photo = models.ForeignKey(ProductBasePhoto, verbose_name='底图')
    style_photo_data = models.ImageField(upload_to='style_photo', verbose_name='样式图片')

    def get_product_id(self):
        self.objects.extra()


class ProductPresetStyle(models.Model):
    product = models.ForeignKey(Product, verbose_name='产品')
    product_preset_style_name = models.CharField(max_length=100, verbose_name='预设样式名称')

    class Meta:
        verbose_name_plural = verbose_name = '产品预设样式'


class ProductPresetStyleItem(models.Model):
    product_preset_style = models.ForeignKey(ProductPresetStyle, verbose_name='产品预设样式')
    product_style = models.ForeignKey(ProductStyle, verbose_name='产品样式')


class QuotationHeader(models.Model):
    creation_date = models.DateTimeField()
    creator = models.ForeignKey(User)
    total_amount = models.DecimalField(max_digits =10, decimal_places=2, default=0)
    short_text = models.TextField(max_length=500, blank=True, verbose_name='备注')


class QuotationItem(models.Model):
    quotation_header = models.ForeignKey(QuotationHeader)
    product = models.ForeignKey(Product)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_text = models.TextField(max_length=500, blank=True, verbose_name='备注')
    product_style = models.ManyToManyField(ProductStyle)

    def get_product_number(self):
        return self.product.product_number

    def get_product_category(self):
        return self.product.product_category

    get_product_number.allow_tags = True
    get_product_category.allow_tags = True
    get_product_category.short_description = '产品类型'










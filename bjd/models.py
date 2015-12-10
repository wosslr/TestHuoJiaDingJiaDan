# coding=utf-8
from django.db import models

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

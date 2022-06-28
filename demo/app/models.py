import numbers
from pyexpat import model
from django.forms import FileField
from django.utils import timezone
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField('Категория товара', max_length=256)
    icon = models.ImageField('Иконка', upload_to='category_icons', blank=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category_products')
    title = models.CharField('Название товара', max_length=256)
    body = models.TextField('Описание', blank=True)
    image = models.ImageField('Фото', upload_to='product_image', blank=True)
    price = models.IntegerField(default=0)
    size = models.IntegerField('Size', default=0, max_length=256, blank=True)
    materials = models.TextField('Material', max_length=256, blank=True)

    



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title








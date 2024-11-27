from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    img = models.ImageField(upload_to='dish_images/', blank=True, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='dishes', verbose_name='Категория')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
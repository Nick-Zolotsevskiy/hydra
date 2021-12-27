from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(
        max_digits=64,
        decimal_places=32,
        validators=[MinValueValidator(0.0)],
        verbose_name='Цена в биткоинах',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} - {self.price} BTC'


class ProductImage(models.Model):
    image = models.ImageField(verbose_name='Файл изображения')
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товара'

    def __str__(self):
        return f'Изображение товара - {self.product.name}'

import datetime

from django.db import models


class Product(models.Model):
    """Класс для создания модели продукта"""
    title = models.CharField(max_length=150, verbose_name='название продукта')
    model = models.CharField(max_length=250, verbose_name='модель продукта')
    product_release_date = models.DateField(default=datetime.date.today, verbose_name='дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_release_date']


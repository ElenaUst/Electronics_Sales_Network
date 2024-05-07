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
        ordering = ['-product_release_date']


class NetworkMember(models.Model):
    """Класс для создания модели поставщика - объекта сети"""
    name = models.CharField(max_length=250, verbose_name='название объекта сети')
    email = models.EmailField(verbose_name='почта объекта сети')
    country = models.CharField(max_length=150, verbose_name='страна объекта сети')
    city = models.CharField(max_length=150, verbose_name='город объекта сети')
    street = models.CharField(max_length=150, verbose_name='улица объекта сети')
    house_number = models.CharField(max_length=50, verbose_name='номер дома объекта сети')
    products = models.ManyToManyField(Product, verbose_name='продукты объекта сети', blank=True)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик объекта сети', null=True, blank=True)
    debt_to_supplier = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='задолженность перед поставщиком',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания объекта сети')

    def __str__(self):
        return f'{self.name}, {self.country}'

    class Meta:
        verbose_name = 'объект сети'
        verbose_name_plural = 'объекты сети'
        ordering = ['-created_at']




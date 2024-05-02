from django.contrib import admin

from network.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение списка продуктов"""
    list_display = ('title', 'model',)

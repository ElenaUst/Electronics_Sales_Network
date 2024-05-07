from django.contrib import admin
from django.urls import path

from network.models import Product, NetworkMember


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Отображение списка продуктов"""
    list_display = ('title', 'model',)


@admin.register(NetworkMember)
class NetworkMemberAdmin(admin.ModelAdmin):
    """Отображение списка объектов сети"""
    list_display = ('name', 'country', 'city', 'supplier', 'debt_to_supplier',)
    list_filter = ('city',)
    actions = ['debt_clearance']

    @admin.action(description="Очистка задолженности перед поставщиком")
    def debt_clearance(self, request, queryset):
        """Функция очистки задолженности перед поставщиком"""
        if self.request.user.is_active:
            count = queryset.update(debt_to_supplier=0)
            self.message_user(request, f'Изменено {count} записей')

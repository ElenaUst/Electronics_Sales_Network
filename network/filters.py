import django_filters
from network.models import NetworkMember


class NetworkMemberFilter(django_filters.rest_framework.FilterSet):
    """Класс для фильтрации объектов сети по стране"""
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains", )

    # CharFilter — специальный фильтр, который позволяет искать совпадения в текстовых полях модели
    class Meta:
        model = NetworkMember
        fields = ("country",)

from rest_framework import serializers
from network.models import Product, NetworkMember


class ProductSerializer(serializers.ModelSerializer):
    """Класс сериализатора для продукта"""
    class Meta:
        model = Product
        fields = '__all__'


class NetworkMemberSerializer(serializers.ModelSerializer):
    """Класс сериализатора для объекта сети"""
    class Meta:
        model = NetworkMember
        fields = '__all__'
        read_only_fields = ['debt_to_supplier']

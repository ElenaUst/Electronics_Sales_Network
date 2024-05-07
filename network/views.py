from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from network.filters import NetworkMemberFilter
from network.models import Product, NetworkMember
from network.paginators import MyPagination
from network.permissions import IsActive
from network.serializers import ProductSerializer, NetworkMemberSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """Класс для создания продукта"""
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductListAPIView(generics.ListAPIView):
    """Класс для просмотра списка продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]
    pagination_class = MyPagination


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра одного продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Класс для изменения продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Класс для удаления продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class NetworkMemberCreateAPIView(generics.CreateAPIView):
    """Класс для создания объекта сети"""
    serializer_class = NetworkMemberSerializer
    permission_classes = [IsAuthenticated, IsActive]


class NetworkMemberListAPIView(generics.ListAPIView):
    """Класс для просмотра списка объектов сети"""
    queryset = NetworkMember.objects.all()
    serializer_class = NetworkMemberSerializer
    filterset_class = NetworkMemberFilter
    permission_classes = [IsAuthenticated, IsActive]


class NetworkMemberRetrieveAPIView(generics.RetrieveAPIView):
    """Класс для просмотра одного объекта сети"""
    queryset = NetworkMember.objects.all()
    serializer_class = NetworkMemberSerializer
    permission_classes = [IsAuthenticated, IsActive]


class NetworkMemberUpdateAPIView(generics.UpdateAPIView):
    """Класс для изменения объекта сети"""
    queryset = NetworkMember.objects.all()
    serializer_class = NetworkMemberSerializer
    permission_classes = [IsAuthenticated, IsActive]


class NetworkMemberDeleteAPIView(generics.DestroyAPIView):
    """Класс для удаления объекта сети"""
    queryset = NetworkMember.objects.all()
    serializer_class = NetworkMemberSerializer
    permission_classes = [IsAuthenticated, IsActive]

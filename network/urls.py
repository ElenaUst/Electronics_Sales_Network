from django.urls import path
from network.apps import NetworkConfig
from network.views import ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, \
    ProductDestroyAPIView, NetworkMemberListAPIView, NetworkMemberCreateAPIView, NetworkMemberRetrieveAPIView, \
    NetworkMemberUpdateAPIView, NetworkMemberDeleteAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/detail/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
    path('', NetworkMemberListAPIView.as_view(), name='network_member_list'),
    path('network/create/', NetworkMemberCreateAPIView.as_view(), name='network_member_create'),
    path('network/detail/<int:pk>/', NetworkMemberRetrieveAPIView.as_view(), name='network_member_detail'),
    path('network/update/<int:pk>/', NetworkMemberUpdateAPIView.as_view(), name='network_member_update'),
    path('network/delete/<int:pk>/', NetworkMemberDeleteAPIView.as_view(), name='network_member_delete'),

]

from django.urls import path
from .views import product_list, order_list, create_order,update_order_status

urlpatterns = [
    path('product_list', product_list, name='product_list'),
    path('order_list', order_list, name='order_list'),
    path('create_order', create_order, name='create_order'),
    path('update_order_status/<int:order_id>/', update_order_status, name='update_order_status'),
]
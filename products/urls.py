from django.urls import path

from order_items import views

urlpatterns = [
    path('products/<int:product_id>/order_items/', views.OrderItemsByProduct.as_view(), name='order_items_by_product'),
]

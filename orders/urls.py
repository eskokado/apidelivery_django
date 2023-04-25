from django.urls import path
from .views import DeliveryView, OrderDelivered

urlpatterns = [
    path('deliveries/', DeliveryView.as_view(), name='deliveries'),
    path('orders/<int:pk>/delivered/', OrderDelivered.as_view(), name="order_delivered"),
]

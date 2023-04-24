from django.urls import path
from .views import DeliveryView

urlpatterns = [
    path('deliveries/', DeliveryView.as_view(), name='deliveries'),
]

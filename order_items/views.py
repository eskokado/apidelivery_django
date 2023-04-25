from django.shortcuts import render
from rest_framework import generics

from order_items.models import OrderItem
from order_items.serializers import OrderItemSerializer


class OrderItemsByProduct(generics.ListAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return OrderItem.objects.filter(product_id=product_id)
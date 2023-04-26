from rest_framework import serializers
from order_items.models import OrderItem
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'discount', 'quantity', 'price')
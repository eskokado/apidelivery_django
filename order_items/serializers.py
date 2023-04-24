from rest_framework import serializers
from order_items.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='order.id', read_only=True)
    product_id = serializers.IntegerField(source='product.id', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order_id', 'product_id', 'discount', 'quantity', 'price']

    def validate(self, data):
        return data

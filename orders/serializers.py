from rest_framework import serializers

from addresses.serializers import AddressSerializer, AddressInfoSerializer
from order_items.models import OrderItem
from order_items.serializers import OrderItemSerializer
from products.serializers import ProductSerializer
from suppliers.serializers import SupplierSerializer
from .models import Order


class CreateDeliveryRequest(serializers.Serializer):
    client_id = serializers.IntegerField(required=True, error_messages={'required': 'Client is Required'})
    supplier_id = serializers.IntegerField(required=True, error_messages={'required': 'Supplier is Required'})
    product_id = serializers.IntegerField(required=True, error_messages={'required': 'Product is Required'})
    discount = serializers.FloatField(required=False)
    quantity = serializers.IntegerField(required=True, error_messages={'required': 'Quantity is Required'})


class ResponseError(serializers.Serializer):
    message = serializers.CharField()
    field = serializers.CharField()


class OrderResponseSerializer(serializers.ModelSerializer):
    address_of_delivery = AddressSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemResponseSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    supplier = SupplierSerializer(read_only=True)
    address_of_delivery = AddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'order_date', 'state_delivery', 'address_of_delivery', 'supplier', 'order_items')


class CreateDeliveryResponse(serializers.Serializer):
    order = OrderResponseSerializer()
    order_items = OrderItemResponseSerializer(many=True)
    errors = serializers.ListField(child=serializers.DictField(), required=False)
    status_code = serializers.IntegerField()


class DeliveryResponseSerializer(serializers.Serializer):
    order = OrderSerializer()
    order_items = OrderItemSerializer(many=True)
    errors = serializers.ListField(child=serializers.DictField(), required=False)
    status_code = serializers.IntegerField()

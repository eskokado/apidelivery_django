from rest_framework import serializers

from order_items.serializers import OrderItemSerializer
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


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CreateDeliveryResponse(serializers.Serializer):
    order = OrderSerializer()
    order_items = OrderItemSerializer(many=True)
    errors = serializers.ListField(child=serializers.DictField(), required=False)
    status_code = serializers.IntegerField()


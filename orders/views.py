from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Order, StateDelivery
from .serializers import CreateDeliveryRequest, OrderSerializer
from .delivery_service import DeliveryService


class DeliveryView(APIView):
    def post(self, request):
        serializer = CreateDeliveryRequest(data=request.data)
        if serializer.is_valid():
            delivery_response_data = DeliveryService.create_delivery(serializer.validated_data)
            return Response(delivery_response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDelivered(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        instance.state_delivery = StateDelivery.DELIVERED.code
        serializer.save(state_delivery=instance.state_delivery)


class OrderCancel(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        instance.state_delivery = StateDelivery.CANCELED.code
        serializer.save(state_delivery=instance.state_delivery)

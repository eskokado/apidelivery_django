from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from accounts.permissions import IsAdminUser, IsAuthenticated
from .models import Order, StateDelivery
from .serializers import CreateDeliveryRequest, OrderSerializer
from .delivery_service import DeliveryService


class DeliveryView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = CreateDeliveryRequest(data=request.data)
        if serializer.is_valid():
            delivery_response_data = DeliveryService.create_delivery(serializer.validated_data)
            return Response(delivery_response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDelivered(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        instance.state_delivery = StateDelivery.DELIVERED.code
        serializer.save(state_delivery=instance.state_delivery)


class OrderCancel(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        instance = self.get_object()
        instance.state_delivery = StateDelivery.CANCELED.code
        serializer.save(state_delivery=instance.state_delivery)


class OrderSearchView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        terms = request.query_params.get('terms', '')

        orders = Order.objects.filter(
            Q(address_of_delivery__client__name__icontains=terms) |
            Q(supplier__name__icontains=terms)
        )

        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)

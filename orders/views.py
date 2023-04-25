import ipdb
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateDeliveryRequest, CreateDeliveryResponse, DeliveryResponseSerializer
from .delivery_service import DeliveryService


class DeliveryView(APIView):
    def post(self, request):
        serializer = CreateDeliveryRequest(data=request.data)
        if serializer.is_valid():
            delivery_response_data = DeliveryService.create_delivery(serializer.validated_data)
            return Response(delivery_response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

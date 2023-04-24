from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateDeliveryRequest, CreateDeliveryResponse
from .delivery_service import DeliveryService


class DeliveryView(APIView):
    def post(self, request):
        serializer = CreateDeliveryRequest(data=request.data)
        if serializer.is_valid():
            delivery_response_data = DeliveryService.create_delivery(serializer.validated_data)
            response_serializer = CreateDeliveryResponse(data=delivery_response_data)
            if response_serializer.is_valid():
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(response_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

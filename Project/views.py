from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Customer,Order
from .serializer import CustomerSerializer,OrderSerializer
from rest_framework import status
import africastalking

# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "203b5555a5e27c9d3d6283b1a944317e86099e9e994631dbbcd348591c409830"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)

# Initialize a service e.g. SMS
sms = africastalking.SMS
# Create your views here.
class CustomerList(APIView):
    def get(self, request, format=None):
        all_customer = Customer.objects.all()
        serializers = CustomerSerializer(all_customer, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  



class OrderList(APIView):
    def get(self, request, format=None):
        all_order = Order.objects.all()
        serializers = OrderSerializer(all_order, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = OrderSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            response = sms.send("Hello Message!", ["+254701796204"])

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
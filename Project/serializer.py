from rest_framework import serializers
from .models import Customer,Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('item', 'price', 'time','customer')

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone_number','orders')
    def create(self, validated_data):
        orders_data = validated_data.pop('orders')
        customer = Customer.objects.create(**validated_data)
        for order_data in orders_data:
            Order.objects.create(order=order **order_data)
        return order

from rest_framework import serializers
from .models import Order, OrderItem


## Serialize Order model
class OrderSerialize(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ["id", "user", "store"]


## Serialize OrderItem model
class OrderItemSerialize(serializers.ModelSerializer): 
    class Meta: 
        model = OrderItem 
        fields = ["id", "order", "item", "quantity"] 

        
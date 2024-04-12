from .models import Order, OrderItem
from .serializers import OrderSerialize, OrderItemSerialize
from rest_framework import viewsets


## Order api class 
class Myorder(viewsets.ModelViewSet): 
    queryset = Order.objects.all() 
    serializer_class = OrderSerialize 


## OrderItem api class 
class MyOrderItem(viewsets.ModelViewSet): 
    queryset = OrderItem.objects.all() 
    serializer_class = OrderItemSerialize 

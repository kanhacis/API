from typing import Any
from django.contrib import admin
from .models import Order, OrderItem
from mystore.models import Mystore


## Register Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "store"]
    list_per_page = 5

    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            user_store = Mystore.objects.get(user=request.user)
            return Order.objects.filter(store=user_store)
        else:
            return super().get_queryset(request) 
        
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return ["user", "store"]
        else:
            return []


## Register OrderItem model
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "item", "quantity"] 
    list_per_page = 5

    def get_queryset(self, request): 
        if request.user.is_staff and not request.user.is_superuser:
            user_store = Mystore.objects.get(user=request.user)
            user_store_order = Order.objects.filter(store=user_store)
            return OrderItem.objects.filter(order__in=user_store_order)
        else:
            return super().get_queryset(request) 
        
    def get_list_filter(self, request): 
        if request.user.is_superuser: 
            return ["order", "item"] 
        else: 
            return [] 

    
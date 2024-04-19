from django.contrib import admin
from .models import Cart, CartItem


## Register Cart model
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "store"]
    list_per_page = 5


## Register CartItem model
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["id", "cart", "item", "quantity"]
    list_per_page = 5
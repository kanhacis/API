from rest_framework import serializers
from .models import Cart, CartItem


## Serialize CartItem 
class CartItemSerialize(serializers.ModelSerializer): 
    price = serializers.DecimalField(max_digits=10, decimal_places=2, source='item.price', read_only=True) 
    item_images = serializers.SerializerMethodField() 
    name = serializers.CharField(source="item.name", read_only=True) 
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = CartItem
        fields = ["id", "cart", "item", "quantity", "price", "name", "total_price", "item_images"]

    def get_item_images(self, obj): 
        item = obj.item 
        images = item.item_images.all()  # item_images is related_name for ItemImage 
        return [image.img.url for image in images] 
    
    def get_total_price(self, obj):
        return obj.quantity * obj.item.price


## Serialize Cart
class CartSerialize(serializers.ModelSerializer):
    # cartItem = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="mycartitem-detail") # used for url of mycartitem
    cart = CartItemSerialize(many=True, read_only=True) # Use the nested serializer
    store_name = serializers.CharField(source="store.name")
    subtotal = serializers.SerializerMethodField(read_only=True)
    
    class Meta: 
        model = Cart 
        fields = ["id", "user", "store", "store_name", "cart", "subtotal"] 

    def get_subtotal(self, obj):
        subtotal = sum(item.quantity * item.item.price for item in obj.cart.all()) 
        return subtotal
    
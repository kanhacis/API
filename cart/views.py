from .models import Cart, CartItem
from .serializers import CartSerialize, CartItemSerialize
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


## Cart api class
class MyCart(viewsets.ModelViewSet):
    serializer_class = CartSerialize

    def get_queryset(self): 
        user_id = self.request.query_params.get("user_id")
        if user_id: 
            return Cart.objects.filter(user=user_id)
        else: 
            return Cart.objects.all() 

    def create(self, request): 
        user_id = request.data.get("user") 
        store_id = request.data.get("store") 
        
        try: 
            existing_cart = Cart.objects.get(user=user_id, store=store_id) 
            return Response({"cart_id": existing_cart.id}, status=status.HTTP_200_OK) 
        
        except Cart.DoesNotExist: 
            serializer = self.get_serializer(data=request.data) 
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


## CartItem api class 
class MyCartItem(viewsets.ModelViewSet): 
    queryset = CartItem.objects.all() 
    serializer_class = CartItemSerialize 
    
    def create(self, request): 
        cart_id = request.data.get("cart")  
        item_id = request.data.get("item") 
        quantity = request.data.get("quantity") 
    
        try: 
            existing_item = CartItem.objects.get(cart=cart_id, item=item_id)   
            existing_item.quantity = quantity 
            existing_item.save() 
            return Response({"msg": "Item quantity increased"}, status=status.HTTP_200_OK)  
        
        except CartItem.DoesNotExist: 
            serializer = self.get_serializer(data=request.data) 
            serializer.is_valid(raise_exception=True) 
            serializer.save() 
            return Response({"msg": "Item added to cart"}, status=status.HTTP_201_CREATED) 
        
    def destroy(self, request, pk=None):
        if pk:
            cartItem = CartItem.objects.get(id=pk)
            cartItem.delete()
            return Response({"msg":"Ited deleted successfully"}, status=status.HTTP_200_OK) 
        

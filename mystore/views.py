from django.shortcuts import render
from .models import Mystore, StoreItem, ReviewItem
from .serializers import MystoreSerialize, StoreItemSerialize, ReviewItemSerialize
from rest_framework import viewsets
from account.models import Addres


# Mystore api class
class Store(viewsets.ModelViewSet):
    serializer_class = MystoreSerialize

    def get_queryset(self):
        try:
            user_city = Addres.objects.filter(user=self.request.user)[0].city
            return Mystore.objects.filter(city=user_city)
        except:
            return Mystore.objects.all() 


# StoreItem api class
class Item(viewsets.ModelViewSet):
    serializer_class = StoreItemSerialize

    def get_queryset(self):
        try:
            user_city = Addres.objects.filter(user=self.request.user)[0].city
            user_city_store = Mystore.objects.filter(city=user_city)
            return StoreItem.objects.filter(store__in=user_city_store)
        except:
            return StoreItem.objects.all()


# ReviewItem api class
class Review(viewsets.ModelViewSet):
    queryset = ReviewItem.objects.all()
    serializer_class = ReviewItemSerialize
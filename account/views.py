## Register api class
# class Register(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

#     def perform_create(self, serializer):
#         user_instance = serializer.save()

#         # Add user to 'staff' group
#         # group = Group.objects.get(name="staff")
#         # user_instance.groups.add(group)
         
#         # Create an address for the new user 
#         Addres.objects.create(user=user_instance)


from django.shortcuts import render, redirect
from .models import User, Contact, Addres
from .serializers import UserSerializer, ContactSerializer, AddressSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from account.models import User
from django.contrib.auth.tokens import default_token_generator
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import logout


## Register api class
class Register(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user_instance = serializer.save()
        Addres.objects.create(user=user_instance)


## Login api class
class Loginview(APIView):
    def post(self, request):
        username = request.data["username"] 
        password = request.data["password"] 
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("Account does not exist")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        
        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user) 
        
        return Response({ 
            "access_token": str(access_token), 
            "refresh_token": str(refresh_token) 
        }) 
        
## Contact api class
class Contact(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

## Address api class
class Address(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer 

    def get_queryset(self):
        try:
            return Addres.objects.filter(user=self.request.user)
        except:
            return Addres.objects.all()
    

## Logout function for admin
def logout_view(request):
  logout(request)
  response = redirect('/admin/login/?next=/admin/account/user/')
  response.delete_cookie('example_cookie')
  return response 

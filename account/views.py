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


from django.shortcuts import redirect
from .models import User, Contact, Addres
from .serializers import UserSerializer, ContactSerializer, AddressSerializer
from rest_framework import viewsets
from django.contrib.auth import logout
from account.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import UserSerializer 
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import Group
from mystore.models import Mystore


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

    def create(self, request):
        email = request.data.get("email")
        subject = request.data.get("subject")

        user = User.objects.get(email=email)
        if user and subject == "Open store":
            user.is_staff = True
            user.save()
            group = Group.objects.get(name="staff")
            user.groups.add(group)

            # Create instance of store for this user
            Mystore.objects.create(user=user)

        # Call the superclass method to continue with regular object creation
        return super().create(request)
        

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

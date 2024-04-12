from django.contrib import admin
from .models import Contact, Addres, User


## Register user model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ## List of fields displayed in admin panel
    list_display = ["id", "username", "email", "contact", "is_staff"]
    search_fields = ["username"]

    ## Function to get a logIn user object
    def get_queryset(self, request):
        if (request.user.is_staff) and (not request.user.is_superuser):
            return User.objects.filter(username=request.user.username)
        else:
            return User.objects.all()
            

## Register contact model
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ## List of fields displayed in admin panel
    list_display = ["email", "contact", "subject"]


## Register admin model
@admin.register(Addres)
class AddressAdmin(admin.ModelAdmin):
    ## List of fields displayed in admin panel
    list_display = ["user", "state", "city", "area"]

    ## Function to get a logIn user address object
    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            return Addres.objects.filter(user=request.user)
        else:
            return super().get_queryset(request)
        
    ## Function to display logIn user in user field
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == "user":
                kwargs["initial"] = request.user.id
                kwargs["disabled"] = True 
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
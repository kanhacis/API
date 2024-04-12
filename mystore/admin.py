from django.contrib import admin
from .models import Mystore, StoreItem, ReviewItem, ItemImage
from django.utils.safestring import mark_safe
from .models import ItemImage


## Register Mystore model 
@admin.register(Mystore) 
class MystoreAdmin(admin.ModelAdmin): 
    list_display = ["id", "user", "name", "contact", "date", "verification"] 
    readonly_fields = ["verification"] 

    ## Function to freeze verification field to is_staff user 
    def get_readonly_fields(self, request, obj=None): 
        if request.user.is_staff and not request.user.is_superuser: 
            return ["verification"] 
        return [] 

    ## Function to filter out logIn user store 
    def get_queryset(self, request): 
        if request.user.is_staff and not request.user.is_superuser: 
            return Mystore.objects.filter(user=request.user) 
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


## Register StoreItem
@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ["id", "store", "name", "type", "standard", "price"]
    list_filter = ["name", "type", "standard", "price"]
    list_per_page = 5

    ## Function to filter out logIn user store items
    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            my_store = Mystore.objects.get(user=request.user)
            return StoreItem.objects.filter(store=my_store)
        else:
            return super().get_queryset(request) 
    
    ## Function to display logIn user store name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == "store":
                my_store = Mystore.objects.get(user=request.user)
                kwargs["queryset"] = Mystore.objects.filter(pk=my_store.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    ## Function to disabled edit & add button
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.is_staff and not request.user.is_superuser:
            form.base_fields['store'].widget.can_add_related = False
            form.base_fields['store'].widget.can_change_related = False
        return form 


## Register ReviewItem 
@admin.register(ReviewItem) 
class ReviewItemAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "item"]

    ## Function to filter out logIn user store items review
    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser: 
            my_store = Mystore.objects.get(user=request.user) 
            store_item = StoreItem.objects.filter(store=my_store) 
            return ReviewItem.objects.filter(item__in=store_item) 
        else:      
            return super().get_queryset(request)


## Register ItemImage
@admin.register(ItemImage) 
class ItemImageAdmin(admin.ModelAdmin): 
    list_display = ["id", "item", "img"] 
    readonly_fields = ["img"] 

    readonly_fields = ["img_image"] 

    def img_image(self, obj): 
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format( 
            url=obj.img.url, 
            width=100, 
            height=100, 
        )) 
    
    img_image.short_description = "Image"
    
    ## Function to filter out ItemImages of current store item
    def get_queryset(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            my_store = Mystore.objects.get(user=request.user)
            store_item = StoreItem.objects.filter(store=my_store)
            return ItemImage.objects.filter(item__in=store_item)
        else:
            return super().get_queryset(request)
        
    ## Function to display only logIn user store items name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_staff and not request.user.is_superuser:
            if db_field.name == "item":
                my_store = Mystore.objects.get(user=request.user)
                kwargs["queryset"] = StoreItem.objects.filter(store=my_store)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    ## Function to disabled edit & add button
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.user.is_staff and not request.user.is_superuser:
            form.base_fields['item'].widget.can_add_related = False
            form.base_fields['item'].widget.can_change_related = False
        return form 


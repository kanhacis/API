from .models import Mystore, StoreItem, ReviewItem, ItemImage
from rest_framework import serializers
from django.db.models import Avg


## Serialize ReviewItem
class ReviewItemSerialize(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True, default="booKStore User")
    
    class Meta:
        model = ReviewItem
        fields = ["id", "user", "username", "item", "rating", "description"]


## Serialize ItemImage
class ItemImageSerialize(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ["id", "item", "img"]


## Serialize StoreItem model
class StoreItemSerialize(serializers.ModelSerializer):
    item_images = ItemImageSerialize(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    user_count = serializers.SerializerMethodField()
    # store_name = serializers.SerializerMethodField(source="store.name", read_only=True)
    item_review = ReviewItemSerialize(many=True, read_only=True)
    
    class Meta:
        model = StoreItem
        fields = ["id", "store", "name", "type", "standard", "price", "itemDesc", "item_review", "item_images", "average_rating", "user_count"]
    
    def get_average_rating(self, obj): 
        average_rating = ReviewItem.objects.filter(item=obj).aggregate(Avg('rating'))['rating__avg']
        return round(average_rating) if average_rating is not None else 0
    
    def get_user_count(self, obj):
        count = ReviewItem.objects.filter(item=obj).count()
        return count
    

## Serialize Mystore model
class MystoreSerialize(serializers.ModelSerializer):
    # storeItem = serializers.StringRelatedField(many=True, read_only=True)
    # storeItem = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # storeItem = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="storeitem-detail") # storeitem -> is a url of (Item view) (StoreItem model)
    
    average_rating = serializers.SerializerMethodField()  # Add this field to calculate average rating
    
    class Meta: 
        model = Mystore
        fields = ["id", "user", "name", "contact", "city", "date", "status", "location", "verification", "image", "average_rating"]
    
    def get_average_rating(self, obj):
        # Calculate average rating for all store items
        total_ratings = 0 
        total_items = 0 
        for store_item in obj.storeItem.all():
            total_ratings += ReviewItem.objects.filter(item=store_item).aggregate(Avg('rating'))['rating__avg'] or 0
            total_items += 1
        
        # Calculate average rating for store if there are items and ratings 
        if total_items > 0: 
            return round(total_ratings / total_items) 
        else: 
            return 0 # Return 0 if there are no items or ratings 
        
 
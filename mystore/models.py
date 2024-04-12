from django.db import models
from account.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


## My store model
class Mystore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    verification = models.BooleanField(default=False, blank=True, null=True)
    image = models.ImageField(upload_to="storeImages/")
    recharge = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


## Store item model 
ITEM_TYPES = ( 
    ("School Book", "School Book"), 
    ("Syllabus Book", "Syllabus Book"), 
    ("College Book", "College Book"), 
    ("Notes", "Notes"), 
    ("Other", "Other"), 
) 
class StoreItem(models.Model): 
    store = models.ForeignKey(Mystore, on_delete=models.CASCADE, related_name="storeItem") 
    name = models.CharField(max_length=100, blank=True, null=True) 
    type = models.CharField(max_length=100, blank=True, null=True, choices=ITEM_TYPES) 
    standard = models.CharField(max_length=255, blank=True, null=True) 
    price = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True) 
    itemDesc = models.TextField(blank=True, null=True) 
    topay = models.PositiveIntegerField(blank=True, null=True) 
    
    def save(self, *args, **kwargs): 
        if self.price is not None: 
            self.topay = int(self.price * 0.05) 
        else: 
            self.topay = None 

        my_store_id = Mystore.objects.get(id=self.store.id) 
        
        if(my_store_id.recharge - self.topay >= 0):
            my_store_id.recharge = my_store_id.recharge - self.topay 
            my_store_id.save()
        else:
            print("Recharge your store")

        super().save(*args, **kwargs) 

    def __str__(self): 
        return self.name 


## Store item images 
class ItemImage(models.Model): 
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE, related_name="item_images") 
    img = models.ImageField(upload_to="storeImages/") 
    
    def __str__(self): 
        return f"Image for {self.item.name}" 


## Review model 
class ReviewItem(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE) 
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    description = models.TextField() 
    created_at = models.DateField(auto_now_add=True) 

    class Meta: 
        unique_together = ('user', 'item') 

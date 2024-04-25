from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mystore import views


router = DefaultRouter()
router.register("mystore", views.Store, basename="mystore")
router.register("storeitem", views.Item, basename="storeitem")
router.register("reviewitem", views.Review, basename="reviewitem")
router.register("images", views.Images, basename="images")
router.register("storerelateditem", views.StoreRelatedItem, basename="storerelateditem")
router.register("itemonly", views.ItemOnly, basename="itemonly")

urlpatterns = [
    path("", include(router.urls))
]
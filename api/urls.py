
from django.contrib import admin 
from django.urls import path, include 
from . import views 
from rest_framework import routers # Generates the URLS for my model. 

router = routers.DefaultRouter() # Instantiate the default router. 
router.register('api', views.ApiView) # Register the views that I have. 

urlpatterns = [
    path('', include(router.urls)) # Creates the nice API html view that we see, no need for additional ex swagger/postman. 
]

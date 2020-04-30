
from django.urls import path, include
from rest_framework import routers
from .views import UploadProfileImage

urlpatterns = [
    path('profileimage/', UploadProfileImage.as_view())
]

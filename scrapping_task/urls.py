from django.urls import path, include
from .views import index, get_user, get_user_info , get_images

urlpatterns = [
    path('', index),
    path('user/', get_user),
    path('search/', get_user_info),
    path('images/', get_images),
]

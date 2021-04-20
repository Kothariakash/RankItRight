from django.contrib import admin
from django.urls import path, include
import scrapping_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scrapping_task.urls')),
]

from django.contrib import admin
from django.urls import path, include

# app_name = 'max'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('max.urls')),
]

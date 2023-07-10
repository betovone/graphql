from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_prueba.urls')),
    path('admin/', admin.site.urls),
]

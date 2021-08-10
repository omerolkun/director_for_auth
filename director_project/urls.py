
from os import name
from django.contrib import admin
from django.urls import path,include
from app_director import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home_page"),
    path('directors/',include('app_director.urls')),
]

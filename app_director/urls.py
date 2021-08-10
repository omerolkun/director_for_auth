from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index_page'),
    path('add_director', views.addDirector,name='add_director_page'),
]
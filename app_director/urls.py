from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('add_director', views.addDirector,name='add_director_page'),
    path('detail_director/<int:idid>',views.detail,name='detail_page'),
    path('edit/<int:yonetmen_no>',views.edit,name='edit_page'),
    path('delete/<int:delete_id>',views.deleteDirector,name='delete_page'),
    path('edit_movie/<int:m_id>',views.editMovie,name='edit_movie_page'),
    path('add_movie/<int:drextor_id>',views.addMovie,name='add_movie_page'),
    
    
]
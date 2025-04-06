from django.urls import path
from . import views

urlpatterns = [   
    path('',views.posts_list,name='posts'),
    path('create-incident/', views.create_incident, name='create_incident'),
    path('create-type-incident/', views.create_type_incident, name='create_type_incident'),
    
]
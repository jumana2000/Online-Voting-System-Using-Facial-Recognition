from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('userRegister/',views.userRegister,name='userRegister'),
    path('read_image/',views.read_image,name='read_image'),
    path('candidate_list/',views.candidate_list,name='candidate_list')
    
]
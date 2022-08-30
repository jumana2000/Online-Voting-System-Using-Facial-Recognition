from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('register_data',views.register_data,name='register_data')
]
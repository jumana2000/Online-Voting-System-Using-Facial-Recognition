from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_index,name='admin_index'),
    path('candidate_register',views.candidate_register,name='candidate_register'),
    path('candidate_register_data',views.candidate_register_data,name='candidate_register_data'),
    path('available_candidates',views.available_candidates,name='available_candidates'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('ad_login',views.ad_login,name='ad_login'),
    path('admin_logout',views.admin_logout,name='admin_logout')
]
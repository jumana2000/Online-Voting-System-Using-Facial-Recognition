from django.urls import path
from . import views

urlpatterns = [
    path('admin_index/',views.admin_index,name='admin_index'),
    path('candidate_register/',views.candidate_register,name='candidate_register'),
    path('candidate_register_data/',views.candidate_register_data,name='candidate_register_data'),
    path('available_candidates/',views.Available_Candidates.as_view(),name='available_candidates'),
    path('view_candidate/<int:pk>/',views.View_Candidate.as_view(),name='view_candidate'),
    path('edit_candidate/<int:pk>/',views.Edit_Candidate.as_view(),name='edit_candidate'),
    path('delete_candidate/<int:pk>/',views.Delete_Candidate.as_view(),name='delete_candidate'),
    path('result/',views.result,name='result'),
    path('user_register/',views.user_register.as_view(),name='user_register'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('ad_login/',views.ad_login,name='ad_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout')
]
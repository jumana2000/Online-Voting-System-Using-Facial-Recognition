from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('candidate_detail/<int:id>/',views.candidate_detail,name='candidate_detail'),
    path('vote/',views.vote,name='vote'),
    path('submit/<int:did>',views.submit,name='submit'),
    path('view_result/',views.view_result,name='view_result')
]
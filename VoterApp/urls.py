from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('candidate_detail/<int:id>/',views.candidate_detail,name='candidate_detail'),
    path('vote/',views.vote,name='vote'),
    path('submit',views.submit,name='submit'),
]
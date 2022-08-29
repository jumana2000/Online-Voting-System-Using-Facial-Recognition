from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('candidate_detail/',views.candidate_detail,name='candidate_detail')
]
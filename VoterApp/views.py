from Dashboard.models import *
from django.shortcuts import render,redirect
from . models import *

# Create your views here.

def index(request):
    data = CandidateRegister.objects.all()
    return render(request,'index.html',{'data':data})

def about(request):
    return render(request,'about.html')

def candidate_detail(request,id):
    data = CandidateRegister.objects.filter(id=id)
    return render(request,'candidate_detail.html',{'data':data})

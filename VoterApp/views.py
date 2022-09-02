from django.http import HttpResponse
from Dashboard.models import *
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.

def index(request):
    data = CandidateRegister.objects.all()
    return render(request,'index.html',{'data':data})

def about(request):
    return render(request,'about.html')

def candidate_detail(request,id):
    data = CandidateRegister.objects.filter(id=id)
    return render(request,'candidate_detail.html',{'data':data})

def vote(request):
    data = CandidateRegister.objects.all()
    return render(request,'vote.html',{'data':data})

def submit(request):
    if request.method == "POST":
        try:
            candidate_name = request.POST.get('candidate_name')
            username = request.POST.get('username')
            count = 1
            data = Vote(candidate_name=candidate_name,username=username,count=count)
            data.save()
            messages.success(request,'Success')
            del request.session['username']
            del request.session['password']
            return redirect('index')
        except KeyError:
            return HttpResponse("Already Voted")
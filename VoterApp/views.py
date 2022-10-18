from django.shortcuts import render,redirect

from Dashboard.models import *
from Accounts.models import *
from .models import *

from django.contrib import messages
from django.db.models.aggregates import Max
import datetime

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

def submit(request,did):
    face_id  = request.session.get('id')
    print(face_id)
    date = datetime.datetime.now()
    
    if VoterRegister.objects.filter(face_id=face_id,date=date).exists():
        messages.error(request, 'Already Voted')
        return redirect('index')
    else:
        vote = CandidateRegister.objects.filter(id=did).values('vote_count')
        for i in vote:
            count = i['vote_count']
        print(count)
        CandidateRegister.objects.filter(id=did).update(vote_count=count+1)
        VoterRegister.objects.filter(face_id=face_id).update(date=date)
        messages.success(request,'Voted Successfully')
        return redirect('index')

def view_result(request):
    data = CandidateRegister.objects.all().aggregate(Max('vote_count'))
    x = data['vote_count__max']
    print(x)
    data = CandidateRegister.objects.filter(vote_count=x)
    return render(request,'view_result.html',{'data':data})
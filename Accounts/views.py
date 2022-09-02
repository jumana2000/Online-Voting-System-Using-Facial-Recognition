from django.shortcuts import render,redirect
from . models import *
from Dashboard.models import *
from django.http import HttpResponse
from Accounts.detection import FaceRecognition
import datetime
# Create your views here.

faceRecognition = FaceRecognition()

def register(request):
    return render(request,'register.html')

def register_data(request):
    if request.method == "POST":
        face_id = request.POST.get('face_id')
        voter_name = request.POST.get('voter_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = VoterRegister(face_id=face_id,voter_name=voter_name,
        age=age,email=email,address=address,username=username,password=password)
        data.save()

        addFace(request.POST['face_id'])
        return redirect('index')
    else:
        return HttpResponse("Not registered")
 

def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('index')

# def adlogin(request):
#     return render(request,'login.html')

def login(request):
    date = datetime.datetime.now()
    face_id = faceRecognition.recognizeFace()
    print(face_id)
    if VoterRegister.objects.filter(date=date,face_id=face_id).exists():
        return HttpResponse("Already voted")
    else:
        data = VoterRegister.objects.filter(face_id=face_id).values('username','password').first()
        request.session['username'] = data['username']
        request.session['password'] = data['password']
        print(data)
        return redirect('greeting' ,str(face_id))

def Greeting(request,face_id):
    date = datetime.datetime.now()
    VoterRegister.objects.filter(face_id=face_id).update(date=date)
    face_id = int(face_id)
    if VoterRegister.objects.filter(face_id = face_id):
        context ={
        'user' : VoterRegister.objects.filter(face_id = face_id),
        }
        candidate_list = CandidateRegister.objects.all()
        data = VoterRegister.objects.filter(face_id=face_id).values('username','password').first()
        request.session['username'] = data['username']
        request.session['password'] = data['password']
        return render(request,'home.html',{'context':context,'candidate_list':candidate_list})
    elif VoterRegister.objects.filter(face_id = 1):
        return HttpResponse("Unauthorised access")
    else:
        return HttpResponse("Unauthorised access")

def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect('index')


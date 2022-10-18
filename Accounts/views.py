from django.shortcuts import render,redirect
from . models import *
from Dashboard.models import *
from django.http import HttpResponse
from Accounts.detection import FaceRecognition

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

def login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if VoterRegister.objects.filter(username=username,password=password).exists():
            data = VoterRegister.objects.filter(username=username,password=password).values('face_id').first()
            request.session['id'] = data['face_id']
            request.session['username'] = username
            request.session['password'] = password

            face_id = faceRecognition.recognizeFace()
           
            return redirect('greeting' ,str(face_id))
        else:
            return render(request,'login.html',{'msg':'Invalid User Credentials'}) 
    else:
        return render(request,'login.html')


def Greeting(request,face_id):
    face_id = int(face_id)
    data1 = VoterRegister.objects.filter(face_id = face_id)
    data = CandidateRegister.objects.all()
    return render(request,'home.html',{'data1':data1,'candidate_list':data})


def logout(request):
    del request.session['id']
    del request.session['username']
    del request.session['password']  
    return redirect('index')  
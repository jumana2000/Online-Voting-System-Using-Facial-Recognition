from django.shortcuts import render,redirect
from . models import *
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
        
        data = VoterRegister(face_id=face_id,voter_name=voter_name,
        age=age,email=email,address=address)
        data.save()

        addFace(request.POST['face_id'])
        return redirect('index')
    else:
        return HttpResponse("Not registered")



def addFace(face_id):
    face_id = face_id
    faceRecognition.faceDetect(face_id)
    faceRecognition.trainFace()
    return redirect('/')
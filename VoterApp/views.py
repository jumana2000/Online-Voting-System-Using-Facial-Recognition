from django.http import HttpResponse
from Dashboard.models import *
from django.shortcuts import render,redirect
from . models import *
import cv2
import os
# Create your views here.

def index(request):
    return render(request,'index.html')

def candidate_list(request):
    data = CandidateRegister.objects.all()
    return render(request,'candidate_list.html',{'data':data})

def read_image(request):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height
    face_detector = cv2.CascadeClassifier('C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    # For each person, enter one numeric face id
    face_id = input('\n enter user id end press <return> ==>  ')
    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0
    while(True):
        ret, img = cam.read()
        img = cv2.flip(img, 1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("C:\\Users\\user\\Desktop\\IROHUB\\Jumana\\OnlineVotingSystem\\OpenCV\\dataset\\User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
            data = UserRegister(my_image="C:\\Users\\user\\Desktop\\IROHUB\\Jumana\\OnlineVotingSystem\\OpenCV\\dataset\\User." + str(face_id) + '.' + str(count) + ".jpg")
            data.save()
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 1: # Take 30 face sample and stop video
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    return redirect('index')
    

def userRegister(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        voterid = request.POST.get('voterid')
        dob = request.POST.get('dob')
        my_image = request.FILES['my_image']
        
        data = UserRegister(username=username,password=password,voterid=voterid,dob=dob,my_image=my_image)
        data.save()
    return HttpResponse("Saved")
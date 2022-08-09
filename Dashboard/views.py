from django.shortcuts import render,redirect
from  . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def admin_index(request):
    return render(request,'admin_index.html')

def candidate_register(request):
    return render(request,'candidate_register.html')

def candidate_register_data(request):
    if request.method == "POST":
        candidate_id = request.POST.get('candidate_id')
        candidate_name = request.POST.get('candidate_name')
        party_name = request.POST.get('party_name')
        member_support = request.POST.get('member_support')
        age = request.POST.get('age')
        email_id = request.POST.get('email_id')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        candidate_photo = request.FILES['candidate_photo']
        party_logo = request.FILES['party_logo']

        data = CandidateRegister(candidate_id=candidate_id,candidate_name=candidate_name,
                                party_name=party_name,member_support=member_support,
                                age=age,email=email_id,mobile=mobile,address=address,
                                candidate_photo=candidate_photo,party_logo=party_logo)
        data.save()

        return redirect('available_candidates')

def available_candidates(request):
    data = CandidateRegister.objects.all()
    return render(request,'available_candidates.html',{'data':data})

def admin_login(request):
    return render(request,'admin_login.html')

def ad_login(request):
    username_a = request.POST.get('username')
    password_a = request.POST.get('password')
    if User.objects.filter(username__contains=username_a).exists():
        user=authenticate(username=username_a,password=password_a)
        request.session['username_a']=username_a
        request.session['password_a']=password_a
        if user is not None:
            login(request,user)
            return redirect('admin_index')
        else:
            return render(request,'admin_login.html',{'msg':'Sorry....invalid user credentials'})
    else:
        return render(request,'admin_login.html',{'msg':'Sorry....invalid user credentials'})
   
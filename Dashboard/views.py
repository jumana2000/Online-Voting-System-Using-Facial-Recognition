from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from  .models import *
from Accounts.models import VoterRegister

from django.db.models.aggregates import Max

# Create your views here.
def admin_index(request):
    count_voter = VoterRegister.objects.all().count()
    count_candidate = CandidateRegister.objects.all().count()
    return render(request,'admin_index.html',{'count_voter':count_voter,'count_candidate':count_candidate})

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

class Available_Candidates(ListView):
    model = CandidateRegister
    template_name = 'available_candidates.html'
    context_object_name = 'data'

class View_Candidate(DetailView):
    model = CandidateRegister
    template_name = 'view_candidate.html'
    context_object_name = 'i'

class Edit_Candidate(UpdateView):
    model = CandidateRegister
    template_name = 'edit_candidate.html'
    fields = [
        "candidate_id",
        "candidate_name",
        "party_name",
        "member_support",
        "age",
        "address",
        "mobile",
        "candidate_photo",
        "party_logo",
        "email"
    ]
    context_object_name = 'obj'
    success_url = reverse_lazy('available_candidates')

class Delete_Candidate(DeleteView):
    model = CandidateRegister
    success_url = reverse_lazy('available_candidates')
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class user_register(ListView):
    model = VoterRegister
    template_name = 'user_register.html'
    context_object_name = 'data'

def result(request):
    data = CandidateRegister.objects.all()
    max_vote = CandidateRegister.objects.all().aggregate(Max('vote_count'))
    print(max_vote)
    x = max_vote['vote_count__max']
    print(x)
    winner = CandidateRegister.objects.filter(vote_count=x)
    print(winner)
    return render(request,'result.html',{'data':data,'winner':winner})

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
   
def admin_logout(request):
    del request.session['username_a']
    del request.session['password_a']
    logout(request)
    return redirect('admin_login')
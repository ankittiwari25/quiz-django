from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import RegisterForm,LoginForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import LoginForm
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request,'login.html')


def register(request):
    form = RegisterForm()



    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            # form.eid = form.cleaned_data['eid']

            form.name = form.cleaned_data['name']
            form.email = form.cleaned_data['email']
            form.password = form.cleaned_data['password']
            form.con_password = form.cleaned_data['con_password']

            # form.image = form.cleaned_data(['image'])
            form.save(commit=True)

            return HttpResponseRedirect('http://127.0.0.1:8000')

    else:
        form = RegisterForm()

    return render(request,"index.html",{"form":form})



def about(request):
    return render(request,"about.html")


def login(request):
    username=request.POST.get('email')
  
    password=request.POST.get('password')
    aa=Register.objects.get(email=username)
    print(aa)
    pwd= Register.objects.only('password').get(email=username).password
    if password!=pwd:
        return HttpResponse('usern and pass is invalid')

    user = Register.objects.get(email=username,password=password)

    if user is not None:

        return render(request,'welcome.html',{"name":aa})
       
    else:

        return HttpResponse('usern and pass is invalid')
        
    return render(request,'login.html',{"form":form})


def logout(request):
    return render(request,'login.html')

def update(request):
    return render(request,'update_profile.html')
    
# def update_profile(request):

#     if request.POST:
#             reg_form = RegisterForm(request.POST)
#             if reg_form.is_valid():
#                 username=form.cleaned_data.get('name')
#                 profile = Register.objects.get(name=username)
#                 reg_form = RegisterForm(request.POST, instance = profile)
#                 reg_form.save() #cleaned indenting, but would not save unless I added at least 6 characters.
#                 return render(request,'welcome.html')
#             else:
#                 profile = Register.objects.get(name)       
#                 reg_form = RegisterForm(instance=profile)
#                 # return render(request,'index.html',{ 'form':reg_form }, context_instance=RequestContext(request))
#                 return HttpResponse("invalid data")

def update_profile(request):
    username=request.POST.get('name')
    email=request.POST.get('email')
    pass1=request.POST.get('password')
    con_pass=request.POST.get('con_password')

    print(username)
    profile = Register.objects.get(email=email)
   
    profile.name = username
    profile.password = pass1
    profile.con_password = con_pass
    profile.save()
    return HttpResponse("ok")


def questions(request,choice):
    print(choice)
    ques = Questions.objects.filter(catagory__exact = choice)
    print(ques)
    return render(request,'questions.html',{'ques':ques})

def home(request):
    choices = Questions.CAT_CHOICES
    print(choices)
    return render(request,
        'homequestions.html',
        {'choices':choices})


def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
        if total==0:
            return render(request,'result.html',{'score':'0','eff':'0.0','total':total})
            
        eff = (score/total)*100

        if score>1:
            return render(request,'advancejava.html',{'score':score})
        else:
            return render(request,'result.html',{'score':score,'eff':eff,'total':total})

    return render(request,'result.html',{'score':score,'eff':eff,'total':total})

def advancejava(request):
    ques =  Advancejava.objects.all()
    print(ques)
    return render(request,'questions.html',{'ques':ques})

    

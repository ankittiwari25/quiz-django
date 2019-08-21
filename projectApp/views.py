from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Register,Semester
from .forms import RegisterForm,LoginForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import LoginForm
from django.contrib import auth

# Create your views here.


def index(request):
    form = LoginForm()

    
    return render(request,"login.html")

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


def checklogin(request):
     form = LoginForm()



     if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            try:

                user = Register.objects.get(email=username,password=password)
                if user is not None:
                #login(request,user )
                
                    return render(request,"welcome.html")
            #form_data = Register.objects.all()
            #return render(request,"welcome.html",{"data":form_data})
            except:
                messages.error(request,'invalid')
             return render(request,'login.html',{'form':form})
            
        else:
            return HttpResponse('usern and pass is invalid')
     form=LoginForm()
     return render(request,'login.html',{"form":form})
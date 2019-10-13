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
    un=request.POST.get('email')
    up=request.POST.get('password')
    v_un =Register.objects.filter(email=un).exists()
    v_pwd = Register.objects.filter(password=up).exists()
    print("---------------------")
    print(un)
    print(up)
    print("---------------------")
    print("##################")
    print(v_un)
    print(v_pwd)
    print("##################")
    if v_un == False and v_pwd == False:
        messages.error(request,"invalid email & password")
        return render(request,'login.html')
    elif v_un==False:
        messages.error(request,"invalid email")
        return render(request,'login.html')
    elif v_pwd == False:
        messages.error(request,"invalid password")
        return render(request,'login.html')
    elif v_un:
        v_pass = Register.objects.only('password').get(email=un).password
        if v_pass==up:
            if Register.objects.get(email=un,password=up):
                aa=Register.objects.get(email=un)
                return render(request,'welcome.html',{'name':aa})
            else:
                messages.error(request,"invalid password")
                return render(request,'login.html')
        else:
            messages.error(request,"invalid email")
            return render(request,'login.html')
        
       

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
    messages.success(request,'Your profile updated successfully')
    return render(request,'update_profile.html')

def updatehome(request):
    return render(request,'welcome.html')

def category(request):
    choices = Questions.CAT_CHOICES
    return render(request,'homequestions.html',{'choices':choices})

def questions(request,ch1):    
    ch = Questions.CAT_CHOICES
    ques = Questions.objects.filter(catagory__exact = ch1)
    return render(request,'questions.html',{'ques':ques,'selected':ch1})

def home(request):
    choices = Questions.CAT_CHOICES
    return render(request,'homequestions.html',{'choices':choices})


def result(request):

    selected=request.POST.get('selected')  #get the category from question.html

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

        #print(score)
        if total==0:
            return render(request,'result.html',{'score':'0','eff':'0.0','total':total})
            
        eff = (score/total)*100

        if score>1:
            print('yes')
           
            if selected == "java":
                return render(request,'advancejava.html',{'score':score})
            if selected == "c":

                return render(request,'advance_C.html',{'score':score})
            if selected == "python":
                return render(request,'advancepython.html',{'score':score})
            if selected == "android":
                return render(request,'advanceandroid.html',{'score':score})
        else:
            return render(request,'result.html',{'score':score,'eff':eff,'total':total})

    return render(request,'result.html',{'score':score,'eff':eff,'total':total})

def advancejava(request):
    ques =  Advancejava.objects.all()
    print(ques)
    return render(request,'questions.html',{'ques':ques})



#level2 result for c language

def cResult(request):

    selected=request.POST.get('selected')  #get the category from question.html

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
            ans.append((C.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        eff = (score/total)*100

    return render(request,'result.html',{'score':score,'eff':eff,'total':total})

def advancec(request):
    ques = C.objects.all()
    print(ques)
    return render(request,'advanceCquestion.html',{'ques':ques})

#level2 result for python language

def pythonResult(request):

    selected=request.POST.get('selected')  #get the category from question.html

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
            ans.append((Advancepython.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        eff = (score/total)*100
    return render(request,'result.html',{'score':score,'eff':eff,'total':total})



def advancepython(request):
    ques =  Advancepython.objects.all()
    print(ques)
    return render(request,'advancePythonquestion.html',{'ques':ques})


#level2 result for python language

def androidResult(request):

    selected=request.POST.get('selected')  #get the category from question.html

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
            ans.append((Advanceandroid.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        eff = (score/total)*100
    return render(request,'result.html',{'score':score,'eff':eff,'total':total})



def advanceandroid(request):
    ques =  Advanceandroid.objects.all()
    print(ques)
    return render(request,'advanceAndroidquestion.html',{'ques':ques})

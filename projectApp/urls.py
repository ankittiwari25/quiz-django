"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('welcome',views.login),
    
    path("register",views.register,name="register"),
    path("about",views.about,name="about"),
    path('logout',views.logout,name="logout"),
    path('update',views.update,name="update"),
    path('updatehome',views.updatehome,name="updatehome"),
    path('update_profile',views.update_profile,name="update_profile"),
    path('home',views.home,name="home"),
    path('result',views.result,name="result"),
    path('advancejava',views.advancejava,name="advancejava"),
    path('advancepython',views.advancepython),
    path('advancec',views.advancec),
    path('cResult',views.cResult),
    path('pythonResult',views.pythonResult),
    url(r'^(?P<ch1>[\w]+)', views.questions, name = 'questions'),
    
]

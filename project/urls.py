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
from django.urls import path,include
from  projectApp import views
from django.conf.urls import url

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("",include("projectApp.urls")),  
    path("welcome",include("projectApp.urls")),  
    path("register",include("projectApp.urls")),
    #path("welcome",include("projectApp.urls")),
    path("about",include('projectApp.urls')),
    path("logout",include('projectApp.urls')),
    path("update",include('projectApp.urls')),
    path('update_profile',include('projectApp.urls')),
    # path('questions',include('projectApp.urls')), 
    # path('home',include('projectApp.urls')),  
    # path(r'^$', include('projectApp.urls')),
    # url(r'^', include('projectApp.urls')),
    path(r'^projectApp/', include('projectApp.urls')),
]

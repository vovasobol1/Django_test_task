"""
URL configuration for videoGenerator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from videoapp.views import generate_video, get_all_requests, homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage , name='generate_video'),
    path('generateVideo/', generate_video, name='generate_video'),
    path('get_all_requests/',get_all_requests , name='get_all_requests'),
]

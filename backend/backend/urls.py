"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from project import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homemain,name = 'homemain'),
    path('home/',views.home,name = 'home'),
    path('random/',views.random_quotes,name='random_quotes'),
    path('search/<int:pk>/',views.search,name='search'),
    path('hook', csrf_exempt(views.hook) ,name='hook'),
    path('played/<int:pk>/',views.played,name='played'),
    path('seat/<int:seatno>/',views.seat,name='seat'),
    
]

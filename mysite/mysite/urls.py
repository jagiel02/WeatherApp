"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from appka.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cities', CityView) #registered cities as CityView

urlpatterns = [
    path('admin/', admin.site.urls, name ='admin'),
    path('', include('appka.urls')),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete-all/', delete_all, name='delete_all'),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', register, name = 'register' ),
    path('rest/', include(router.urls)),


]

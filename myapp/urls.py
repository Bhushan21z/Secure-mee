from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_page),
    path('logout',views.logout,name='logout'),
    path('add',views.add_page,name='add'),
    path('get',views.get_page,name='get'),
    path('otp',views.get_otp,name='otp'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
]

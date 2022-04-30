from ast import Pass
from email.mime import application
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect

from django.conf import settings
from django.core.mail import send_mail

from .models import Passwords
from .models import Store
from .models import NewUser
#import requests
import random


def home_page(request):
    Store.objects.all().delete()
    return render(request,"index.html")

def logout(request):
    Store.objects.all().delete()
    context_data={
        "submitted": False,
        "error": False,
    }
    check=NewUser.objects.filter(Status=True)
    if(request.method=='POST'):
        check=NewUser.objects.filter(Status=True)
        if(len(check)!=0):
            check[0].Status=False
            check[0].save()
            return render(request,"index.html")
        else:
            return render(request,"index.html")
    return render(request,"index1.html",context_data)

def add_page(request):
    Store.objects.all().delete()
    context_data={
        "submitted": False,
        "error": False
    }
    check=NewUser.objects.filter(Status=True)
    check_id=check[0].u_id
    if(request.method=='POST'):
        
        data=request.POST
        app_name=data['app_name']
        user_name=data['user_name']
        pass_word=data['pass_word']
        
    
        try:
            obj=Passwords(u_id=check_id,application_name=app_name,username=user_name,key=pass_word)
            obj.save()
            context_data["submitted"]=True
            
        except:
            context_data["error"]=True
        
    else:
        print("NO data found")
        
    database={}
    check=NewUser.objects.filter(Status=True)
    if(len(check)!=0):
        check_id=check[0].u_id
        rows=Passwords.objects.filter(u_id=check_id)
        database["rows"]=rows
        
        
    if context_data["submitted"]:
        return render(request,"index1.html",database)
    else:    
        return render(request,"index2.html",database)


def get_otp(request):
    
    row=Store.objects.all()
    database={
        "submitted":False,
        "password_get":"secured"
    }
    check=NewUser.objects.filter(Status=True)
    if(len(check)!=0):
        check_id=check[0].u_id
        rows=Passwords.objects.filter(u_id=check_id)
        database["rows"]=rows
        
    if(request.method=='POST'):
        
        data3=request.POST
        otp=data3['OTP']
    
    if(otp==row[0].otp_t):
        database["password_get"]=row[0].key
        Store.objects.all().delete()
        database["submitted"]=True
        
    return render(request,"index4.html",database)


def get_page(request):
    
    Store.objects.all().delete()
    context_data={
        "submitted": False,
        "error": False
    }
    pass_word="Error_Pass"
    if(request.method=='POST'):
        app_name2 = request.POST.get('app_name1')
        user_name2= request.POST.get('user_name1')
        
    
        try:
            number = random.randint(1111,9999)
            print(number)
            otp_e=str(number)
            row_seacrh=Passwords.objects.filter(application_name=app_name2,username=user_name2)
            pass_word2=row_seacrh[0].key
            obj=Store(application_name=app_name2,username=user_name2,key=pass_word2,otp_t=otp_e)
            obj.save()
            context_data["submitted"]=True
            
        except:
            context_data["error"]=True
        
    else:
        print("NO data found")
    
    database={}
    check=NewUser.objects.filter(Status=True)
    if(len(check)!=0):
        check_id=check[0].u_id
        rows=Passwords.objects.filter(u_id=check_id)
        database["rows"]=rows
    
    
    
    if context_data["submitted"]:
        check=NewUser.objects.filter(Status=True)
        email=check[0].Email
        subject = 'Secure Me'
        message = f'Your OTP is '+otp_e
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,"index4.html",database)
    else:    
        return render(request,"index3.html",database)
    
    
def signup(request):
    Store.objects.all().delete()
    context_data={
        "submitted": False,
        "error": False
    }
    
    if(request.method=='POST'):
        user_data=request.POST
        Name=user_data['Name']
        Email=user_data['Email']
        Password=user_data['Password']
        
    
        try:
            obj_new=NewUser(Name=Name,Email=Email,Password=Password)
            obj_new.save()
            context_data["submitted"]=True
            
        except:
            context_data["error"]=True
        
    else:
        print("NO data found")
    if context_data["submitted"]:
        return render(request,"login.html")
    else:    
        return render(request,"signup.html")
    
    
def login(request):
    Store.objects.all().delete()
    context_data={
        "submitted": False,
        "error": False
    }
    check=NewUser.objects.filter(Status=True)
    
    if(len(check)!=0):
        check[0].Status=False
        check[0].save()
        context_data["Name"]=check[0].Name
            
    if(request.method=='POST'):
        user_data=request.POST
        Name=user_data['Name']
        Password=user_data['Password']
        print("post done")
        
    
        try:
            obj_new=NewUser.objects.filter(Name=Name,Password=Password)
            print(len(obj_new))
            print(obj_new[0].Status)
            obj_new[0].Status=True
            obj_new[0].save()
            print("Done")
            context_data["submitted"]=True
            
        except:
            context_data["error"]=True
        
    else:
        print("NO data found")
    
    if context_data["submitted"]:
        return render(request,"index1.html",context_data)
    else:    
        return render(request,"login.html")
    
    
    
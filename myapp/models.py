from enum import unique
from django.db import models

import uuid

class NewUser(models.Model):
    Status=models.BooleanField(default=False)
    u_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=200)
    Password=models.CharField(max_length=100)
    

class Passwords(models.Model):
    u_id=models.CharField(max_length=100, blank=True, default="0")
    application_name=models.CharField(max_length=500)
    username=models.CharField(max_length=100)
    key=models.CharField(max_length=500)
    
class Store(models.Model):
    u_id=models.CharField(max_length=100, blank=True, default="0")
    application_name=models.CharField(max_length=500)
    username=models.CharField(max_length=100)
    key=models.CharField(max_length=500)
    otp_t=models.CharField(max_length=4,default="0000")

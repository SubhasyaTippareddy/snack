from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_cook=models.BooleanField(default=False)
class Student(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    sid= models.CharField(max_length=8,blank=False,primary_key=True)
    sname=models.CharField(max_length=50,blank=False)
    password=models.CharField(max_length=20,blank=False)
    def __str__(self):
        return self.user.sname
class Cook(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    cname=models.CharField(max_length=25,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    def __str__(self):
        return self.user.cname
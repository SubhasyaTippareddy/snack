from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# class User(AbstractUser):
#     is_student=models.BooleanField(default=False)
#     is_cook=models.BooleanField(default=False)
# class Student(models.Model):
#     user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     sid= models.CharField(max_length=8,blank=False,primary_key=True)
#     sname=models.CharField(max_length=50,blank=False)
#     password=models.CharField(max_length=20,blank=False)
#     def __str__(self):
#         return self.user.sname
# class Cook(models.Model):
#     user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     cname=models.CharField(max_length=25,blank=False)
#     email=models.EmailField(max_length=100,blank=False)
#     def __str__(self):
<<<<<<< HEAD
#         return self.user.cname
=======
#         return self.user.cname

# class foodDetails(models.Model):
#     foodID=models.CharField(max_length=5,blank=False,primary_key=True)
#     foodName=models.CharField(max_length=100,blank=False)
#     meal_type=models.CharField(max_length=20,blank=False)
#     foodimage=models.FileField(upload_to='static/images')
#     is_veg = models.BooleanField(blank=False)

#     def __str__(self):
#         return self.foodName
>>>>>>> fb809021c83827487f7e5ddac491488de99ce473

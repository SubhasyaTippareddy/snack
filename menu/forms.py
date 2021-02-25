from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import User,Student,Cook
class StudentRegistrationForm(UserCreationForm):
    username=forms.CharField(required=True)
    sname=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model=User
    @transaction.atomic
    def save(self):
       user=super().save(commit=False)
       user.is_student=True
       user.save()
       print(user)
       print(user.username)
       print(user.password)
       stud=Student.objects.create(user=user)
       print(Student)
       stud.roll_number=self.cleaned_data.get('sname')
       stud.save()
       return user
class CookRegistrationForm(UserCreationForm):
    username=forms.CharField(required=True)
    email=forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model=User
    @transaction.atomic
    def save(self):
       user=super().save(commit=False)
       user.is_cook=True
       user.save()
       cook=Cook.objects.create(user=user)
       cook.email=self.cleaned_data.get('username')
       cook.save()
       return user.username
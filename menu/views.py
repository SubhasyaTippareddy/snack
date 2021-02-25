from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from .forms import StudentRegistrationForm,CookRegistrationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm

def menu(request):
    context={}
    return render(request,'./index.html',context)

def breakFast(request):
    return render(request,'./breakfast.html')

def Cook(request):
    return render(request,'./cook_orders.html')

def Cart(request):
    return render(request,'./cart.html')


def forgotpassword(request):
    context={}
    return render(request,'./forgotpassword.html')

class student_register(CreateView): #studentRegistration
    model= User
    form_class=StudentRegistrationForm
    template_name='./student_register.html'
    def get_success_url(self):
        return reverse('studentlogin')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class cook_register(CreateView): #CookRegistration
    model= User
    form_class=CookRegistrationForm
    template_name='./cook_register.html'
    def get_success_url(self):
        return reverse('chefLogin')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

#login -1
def studentLogin(request):
        if(request.method=='POST'):
            form=AuthenticationForm(data=request.POST)
            print(form)
            print(request.POST.get('username'))
            print(request.POST.get('password'))
            print(form.is_valid())
            if(form.is_valid()):
                username=request.POST.get('username')
                password=request.POST.get('password')
                print(username)
                print(password)
                user=authenticate(username=username,password=password)
                print(user)
                print(user)
                if user is not None:
                        login(request,user)
                        return redirect('menu')
            else:
                return HttpResponse("Invalid Details given. Please re-enter")
        return render(request, './Student.html',context={'form':AuthenticationForm()})   
#login - 2
def chefLogin(request):
    if(request.method=='POST'):
            form=AuthenticationForm(data=request.POST)
            print(form)
            print(request.POST.get('username'))
            print(request.POST.get('password'))
            print(form.is_valid())
            if(form.is_valid()):
                username=request.POST.get('username')
                password=request.POST.get('password')
                print(username)
                print(password)
                user=authenticate(username=username,password=password)
                print(user)
                print(user)
                if user is not None:
                        login(request,user)
                        return redirect('cook')
            else:
                return HttpResponse("Invalid Details given. Please re-enter")
        
    context={'form':AuthenticationForm()}
    return render(request,'./Chef.html',context)

def logout_student(request):
    logout(request)
    return redirect('studentlogin')

def logout_cook(request):
    logout(request)
    return redirect('cheflogin')

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
#from menu.forms import StudentForm
#def home(request):
    #return HttpResponse("Hey this is home!")
def menu(request):
    return render(request,'./index.html') #./ to go to the root and index.html is the file name
def studentLogin(request):
    return render(request,'./Student.html')
def chefLogin(request):
    return render(request,'./Chef.html')
def forgotpassword(request):
    return render(request,'./forgotpassword.html')
def breakFast(request):
    return render(request,'./breakfast.html')
def Cart(request):
    return render(request,'./cart.html')
def Cook(request):
    return render(request,'./cook.html')
'''
def student_login(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is inactive")
        else:
            return HttpResponse("Invalid Details given.")
'''


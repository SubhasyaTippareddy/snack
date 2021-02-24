from django.shortcuts import render
from django.http import HttpResponse

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


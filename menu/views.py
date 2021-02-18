from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hey this is home!")
def menu(request):
    return render(request,'./index.html')
def login(request):
    return render(request,'./login.html')
def main(request):
    return render(request,'./main.html')

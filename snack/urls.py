"""snack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from menu import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/',views.home,name='home'),
    path('menu/',views.menu,name='menu'), #views here is the file name in menu folder". menu"for calling the func menu in the view folder
    path('',views.studentLogin,name='studentlogin'), 
    path('login/chef',views.chefLogin, name='cheflogin'),
    path('login/student/forgotpassword',views.forgotpassword,name='fp'),
    path('menu/breakfast',views.breakFast,name='breakfast'),
    path('menu/cart',views.Cart,name='cart'),
    
]

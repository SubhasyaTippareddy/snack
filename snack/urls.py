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
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #admin
    path('admin/', admin.site.urls),

    #path('home/',views.home,name='home'),

    #register
    path('cook_register',views.cook_register.as_view(),name='cookregister'),
    path('student_register/',views.student_register.as_view(), name='studentregister'),

    #login
    path('',views.studentLogin,name='studentlogin'),
    path('cheflogin/',views.chefLogin, name='cheflogin'),
    path('login/student/forgotpassword',views.forgotpassword,name='fp'),

    #logout
    path('slogout/',views.logout_student,name='studentlogout'),
    path('clogout/',views.logout_cook,name='cooklogout'),

    #menu and submenus
    path('menu/',views.menu,name='menu'), #student afterlogin
    path('menu/breakfast',views.breakFast,name='breakfast'),
    path('menu/lunch',views.lunch,name='lunch'),

    #cart
    path('cart',views.Cart,name='cart'),

    path('add_to_cart/<uuid:food_id>',views.add_to_cart, name='add_to_cart'),
    #cook_views
    path('cook_orders',views.Cook,name='cook'), #cook after login
    
    path('accounts',include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
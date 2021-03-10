from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from .forms import StudentRegistrationForm,CookRegistrationForm
from .models import User,Food,CartItem,Student,Order,OrderItem
from django.contrib.auth.forms import AuthenticationForm

#menu
def menu(request):
    context={'user':request.user}
    return render(request,'./index.html',context)
#submenus
def breakFast(request):
    return render(request,'./breakfast.html',context={'food_breakfast':Food.objects.filter(meal_time='breakfast'),'user':request.user})

def lunch(request):
    return render(request,'./lunch.html',context={'food_lunch':Food.objects.filter(meal_time='lunch'),'user':request.user})

def snacks(request):
    return render(request,'./snacks.html',context={'food_snacks':Food.objects.filter(meal_time='snacks'),'user':request.user})

def beverages(request):
    return render(request,'./beverages.html',context={'food_beverages':Food.objects.filter(meal_time='beverages'),'user':request.user})

def chips(request):
    return render(request,'./chips.html',context={'food_chips':Food.objects.filter(meal_time='chips'),'user':request.user})

#cook_orders
def Cook(request):
    return render(request,'./cook_orders.html')

#student_order
def Cart(request):
    student=Student.objects.get(user=request.user)
    tot=0
    citems=CartItem.objects.filter(student=student)
    for i in citems:
        tot+=i.get_total
    context={'items':citems,'total':tot}
    return render(request,'./cart.html',context)

def add_item(request, cart_item_id):
    cartitem=CartItem.objects.get(cart_item_id=cart_item_id)
    print(cartitem)
    cartitem.quantity=cartitem.quantity+1
    cartitem.save()
    return redirect('cart')

def subtract_item(request, cart_item_id):
    cartitem=CartItem.objects.get(cart_item_id=cart_item_id)
    print(cartitem)
    cartitem.quantity=cartitem.quantity-1
    cartitem.save()
    return redirect('cart')

def remove_item(request, cart_item_id):
    cartitem=CartItem.objects.filter(cart_item_id=cart_item_id)
    cartitem.delete()
    return redirect('cart')


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
                if user is not None:
                        login(request,user)
                        return redirect('cook')
            else:
                return HttpResponse("Invalid Details given. Please re-enter")
        
    context={'form':AuthenticationForm()}
    return render(request,'./Chef.html',context)
#add_to_cart views
def add_to_cart_breakfast(request, food_id):
    food=Food.objects.get(food_id=food_id)
    student=Student.objects.get(user=request.user)
    citems=CartItem.objects.filter(food=food,student=student)
    if citems.exists()==False:
        print(citems)
        cartitem=CartItem()
        cartitem.food=food
        cartitem.student=student
        cartitem.save()
        print(cartitem)
    return redirect('breakfast')

def add_to_cart_lunch(request, food_id):
    food=Food.objects.get(food_id=food_id)
    student=Student.objects.get(user=request.user)
    citems=CartItem.objects.filter(food=food,student=student)
    if citems.exists()==False:
        print(citems)
        cartitem=CartItem()
        cartitem.food=food
        cartitem.student=student
        cartitem.save()
        print(cartitem)
    return redirect('lunch')

def add_to_cart_snacks(request, food_id):
    food=Food.objects.get(food_id=food_id)
    student=Student.objects.get(user=request.user)
    citems=CartItem.objects.filter(food=food,student=student)
    if citems.exists()==False:
        print(citems)
        cartitem=CartItem()
        cartitem.food=food
        cartitem.student=student
        cartitem.save()
        print(cartitem)
    return redirect('snacks')

def add_to_cart_beverages(request, food_id):
    food=Food.objects.get(food_id=food_id)
    student=Student.objects.get(user=request.user)
    citems=CartItem.objects.filter(food=food,student=student)
    if citems.exists()==False:
        print(citems)
        cartitem=CartItem()
        cartitem.food=food
        cartitem.student=student
        cartitem.save()
        print(cartitem)
    return redirect('beverages')

def add_to_cart_chips(request, food_id):
    food=Food.objects.get(food_id=food_id)
    student=Student.objects.get(user=request.user)
    citems=CartItem.objects.filter(food=food,student=student)
    if citems.exists()==False:
        print(citems)
        cartitem=CartItem()
        cartitem.food=food
        cartitem.student=student
        cartitem.save()
        print(cartitem)
    return redirect('chips')

def confirm_order(request):
    #student=Student.objects.get(user=request.user)
    cartitems=CartItem.objects.filter(student__user=request.user)
    orderlist=[]
    for item in cartitems:
        order_item=OrderItem()
        order_item.food=item.food
        order_item.quantity=item.quantity
        order_item.save()
        print(order_item)
        orderlist.append(order_item)
        item.delete()
    order=Order()
    order.student=Student.objects.get(user=request.user)
    for ele in orderlist:
        order.orderitem.add(ele)
    print(orderlist)
    order.save()
    return redirect('menu')

def logout_student(request):
    logout(request)
    return redirect('studentlogin')

def logout_cook(request):
    logout(request)
    return redirect('cheflogin')

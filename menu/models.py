from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_cook=models.BooleanField(default=False)
    person_name=models.CharField(max_length=100)
    
# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    sname= models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.sname

class Cook(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.EmailField(max_length=100,blank=False)

    def __str__(self):
        return self.user

class Combo(models.Model):
    comboname=models.CharField(max_length=10)
    price=models.FloatField()
    noOfItems=models.PositiveIntegerField()
    def __str__(self):
        return self.comboname

class Food(models.Model):
	fname = models.CharField(max_length=200)
	price = models.FloatField()
	fimage = models.ImageField(null=True, blank=True, upload_to='static/images/')
	is_veg=models.BooleanField(default=True)
	time=[('breakfast','breakfast'),('lunch','lunch'),('snacks','snacks'),('beverages','beverages'),('chips','chips')]   
	meal_time=models.CharField(max_length=50,choices=time) #choices - Breakfast,Lunch,Snacks,Beverages
	combo = models.ForeignKey(Combo,on_delete=models.SET_NULL, null=True, blank=True)
	def __str__(self):
		return self.fname
	@property
	def imageURL(self):
		try:
			url = self.fimage.url
		except:
			url = ''
		return url

class Order(models.Model):
	Student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
	complete = models.BooleanField(default=False)
	date_ordered = models.DateTimeField(auto_now_add=True)
	transaction_id = models.CharField(max_length=100, null=True)
    

	def __str__(self):
		return str(self.id)
		

	@property
	def get_cart_total(self):
		fooditems = self.orderitem_set.all()
		total = sum([item.get_total for item in fooditems])
		return total 

	@property
	def get_cart_items(self):
		fooditems = self.orderitem_set.all()
		total = sum([item.quantity for item in fooditems])
		return total 

class CartItem(models.Model):
	food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.food.price * self.quantity
		return total

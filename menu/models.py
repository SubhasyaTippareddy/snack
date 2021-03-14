from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_cook=models.BooleanField(default=False)
    person_name=models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    sname= models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.user.username

    def getName(self):
        return self.sname

class Cook(models.Model): 
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.EmailField(max_length=100,blank=False)

    def __str__(self):
        return self.user.username


class Food(models.Model):
	food_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	fname = models.CharField(max_length=200)
	price = models.FloatField()
	fimage = models.ImageField(null=True, blank=True, upload_to='static/images/')
	is_veg=models.BooleanField(default=True)
	time=[('breakfast','breakfast'),('lunch','lunch'),('snacks','snacks'),('beverages','beverages'),('chips','chips')]   
	meal_time=models.CharField(max_length=50,choices=time) #choices - Breakfast,Lunch,Snacks,Beverages

	def __str__(self):
		return self.fname
	@property
	def imageURL(self):
		try:
			url = self.fimage.url
		except:
			url = ''
		return url

class Combo(models.Model):
	combo_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	comboname=models.CharField(max_length=200) 
	price=models.FloatField()
	comboitem = models.ManyToManyField(to=Food)
	#noOfItems=models.PositiveIntegerField()
	#manytomany food
	def __str__(self):
		return self.comboname
	
	@property
	def get_food_items(self):
		food_list=[]
		for food in self.comboitem.all():
			food_list.append(food)
		return food_list
		
	@property
	def get_combo_dict(self):
		combo_dict={
			'combo_id':self.combo_id,
			'price':self.price,
			'food_items': [food.fname for food in self.comboitem.all()],
			'combo_name':self.comboname
		}
		return combo_dict


class CartItem(models.Model):
	cart_item_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
	student= models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
	# order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=1,null=True, blank=True)
    
	def __str__(self):
		return self.food.fname
	@property
	def get_total(self):
		total = self.food.price * self.quantity
		return total

class OrderItem(models.Model):
	food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=1, null=True, blank=True)
	orderitem_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	def __str__(self):
		return str(self.food.fname)

	@property
	def get_total(self):
		total = self.food.price * self.quantity
		return total

class Order(models.Model):
	trans_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
	orderitem = models.ManyToManyField(to=OrderItem)
	complete = models.BooleanField(default=False)
	date_ordered = models.DateTimeField(auto_now_add=True)

    

	def __str__(self):
		return str(self.id)
		

	@property
	def get_cart_total(self):
		fooditems = self.orderitem.all()
		total = sum([item.get_total for item in fooditems])
		return total 

	@property
	def get_cart_items(self):
		fooditems = self.orderitem.all()
		total = sum([item.quantity for item in fooditems])
		return total 

	def get_dict(self):
		d={
			'trans_id':self.trans_id,
			'student':self.student.user.username,
			'order_items': [{'food_name':item.food.fname, 'food_price':item.food.price, 'quantity':item.quantity } for item in self.orderitem.all()],
			'date':self.date_ordered,
			'total_price':self.get_cart_total
		}
		return d


from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
	user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	name=models.CharField(max_length=200, null=True)
	email=models.CharField(max_length=200,null=True)
	phone=models.CharField(max_length=10, null=False)
	address=models.CharField(max_length=100)
	profile_pic = models.ImageField(upload_to='static/image',null=True,blank=True, default='sanji.jpg')
	date_created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Tags(models.Model):
	name=models.CharField(max_length=200, null=True)
	

	def __str__(self):
		return self.name



class Product(models.Model):
	CATEGORY=(
		('Indoor','Indoor'),
		('Outdoor','Outdoor')
		)
	name=models.CharField(max_length=200, null=True)
	price=models.FloatField(max_length=10, null=False)
	category=models.CharField(max_length=200, choices=CATEGORY)
	description=models.CharField(max_length=200, blank=True)
	date_created=models.DateTimeField(auto_now_add=True)
	tag=models.ManyToManyField(Tags)

	def __str__(self):
		return self.name





class Order(models.Model):

	STAUTUS = (
		('Pending','Pending'),
		('out for deliver', 'out for delivery'),
		('Delivered','Delivered')
		)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
	product= models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
	date_created=models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=200, null=True, choices=STAUTUS)

	def __str__(self):
		return self.product.name




		
	
		
	


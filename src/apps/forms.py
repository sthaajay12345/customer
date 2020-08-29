from django.forms import ModelForm
from django import forms
from .models import Order,Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
	class Meta:
		model=Order
		fields = '__all__'


class CustomerForm(ModelForm):
	class Meta:
		model=Customer
		fields='__all__'
		exclude=['user']
		

class CreateUserForm(UserCreationForm):
	email=forms.EmailField(max_length=100, help_text='add a valid email address')
	class Meta:
		model=User
		fields = ['username','email','password1','password2']
	
	
	

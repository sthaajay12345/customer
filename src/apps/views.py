from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .filters import OrderFilter
from .decorators import unauthenticated_user,allowed_users,admin_only

@login_required(login_url = 'apps:login')
@admin_only
def home(request):
	orders=Order.objects.all()
	customer=Customer.objects.all()
	total_cus = customer.count()
	total_order=orders.count()
	delivered=orders.filter(status='Delivered').count()
	pending=orders.filter(status='Pending').count()

	context = {'order':orders, 'customers':customer,'total_customer':total_cus,
	 'total_order':total_order, 'delivered':delivered, 'pending':pending}
	return render(request,'dashboard.html', context)

@login_required(login_url = 'apps:login')
@allowed_users(allowed_roles=['admin'])
def product(request):
	products = Product.objects.all()
	return render(request, 'product.html', {'product':products})

@login_required(login_url = 'apps:login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	myFilter=OrderFilter(request.GET,queryset=orders)
	orders=myFilter.qs
	total_order=orders.count()
	context = {'customer':customer,'order':orders,'total_order':total_order,'myFilter':myFilter}
	return render(request, 'customer.html',context)
	
@login_required(login_url = 'apps:login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
	OrderFormSet= inlineformset_factory(Customer,Order, fields=('product','status'))
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	if request.method == 'POST':
		formset = OrderFormSet(request.POST,instance=customer)
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(reverse('apps:home'))
	context={'formset':formset }
	return render(request, 'order_form.html', context)

@login_required(login_url = 'apps:login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk ):
	order=get_object_or_404(Order,id=pk)
	form = OrderForm(request.POST or None, request.FILES or None, instance=order)
	if form.is_valid():
		form.save()
		return redirect('apps:home')

	context={'forms':form}
	return render(request, 'order_form.html', context)


@login_required(login_url = 'apps:login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	order=Order.objects.get(id=pk)
	if request.method =="POST":
		order.delete()
		return redirect('apps:home')

	context={'item':order}
	return render(request, 'delete.html',context)


@unauthenticated_user
def user_register(request):
	
	form=CreateUserForm(request.POST) 
	if request.method == "POST":
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = form.cleaned_data.get('username')
			group=Group.objects.get(name='customer')
			user.groups.add(group)
			messages.success(request,'Account was create for  ' + username)
			return redirect('apps:login')
	context={'form':form}
	return render(request,'register.html', context)

	
@unauthenticated_user
def loginpage(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user = authenticate(request, username=username,password=password)

		if user is not None:
			login(request, user)
			return redirect('apps:home')

		else:
			messages.info(request,'username or password is incorrect')

	context={}
	return render(request,'login.html',context)



		

def logoutuser(request):
	logout(request)
	return redirect('apps:login')


def userpage(request):
	context={}
	return render(request,'user.html',context)
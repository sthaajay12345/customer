from django.urls import path
from .import views

app_name="apps"
urlpatterns = [
	path('',views.home, name="home"),
	path('product/',views.product, name="product"),
	path('customer/<str:pk>/',views.customer, name="customer"),
	path('create_order/<str:pk>/', views.createOrder, name="create_order"),
	path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
	path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
	path('register/',views.user_register, name='register'),
	path('login/',views.loginpage, name='login'),
	path('logout/',views.logoutuser, name='logout'),
	path('userpage/',views.userpage, name='userpage'),

]
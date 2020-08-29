from django.urls import path

from django.conf.urls import url
from django.contrib.auth import views as auth_views
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
	path('account_setting/',views.account_setting, name='account_setting'),

	path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="reset_password"),
	path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name="password_reset_done"),
	
	path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name="password_reset_complete"),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),




]
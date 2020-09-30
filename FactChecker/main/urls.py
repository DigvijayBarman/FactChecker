from django.urls import path, include
from django.contrib import admin
from main import views

urlpatterns = [
	path('', views.home, name='home'),
	path('verified/', views.verified, name='verified'),
	path('fake/', views.fake, name='fake'),
	path('results/', views.results, name='results'),
	# path('submit/', views.submit, name='submit'),
	# path('userpage/', views.userpage, name='userpage'),
]
from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	return render(request, 'main/index.html')

def verified(request): #True
	return render(request, 'main/true.html')

def fake(request): #Fake
	return render(request, 'main/false.html')

# def submit(request): #Unknown
# 	return render(request, 'main/unverified.html')

# def userpage(request):
# 	return render()


def results(request):
	return render(request, 'main/results.html')
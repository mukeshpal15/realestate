from django.shortcuts import render
from django.conf import  settings
from .models import *
# Create your views here.
def index(request):
	return render(request, 'index.html',{})
def properties(request):
	return render(request, 'properties.html', {})

def blog(request):
	return render(request, 'blog.html', {})
def about(request):
	return render(request, 'about.html', {})
def property_detail(request):
	return render(request, 'property-details.html', {})
def contact(request):
	return render(request, 'contact.html', {})
def registration(request):
	return render(request, 'registration.html', {})
def login(request):
	return render(request, 'login.html', {})
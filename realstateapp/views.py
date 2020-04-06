from django.shortcuts import render, redirect
from django.conf import  settings
from .models import *
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages

import uuid
import string
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




def agent_signup(request):
	if request.method=="POST":
		n= request.POST.get('name')
		g= request.POST.get('gender')
		e= request.POST.get('email')
		ad= request.POST.get('address')
		c = request.POST.get('city')
		ph= request.POST.get('phone')
		aa=request.POST.get('aadhar')
		status=0
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]

		if agent_account.objects.filter(email=e).exists():
			message= 'User Already Exist'
			return render(request,'registration.html',{'message':message})

		elif agent_account.objects.filter(phone=ph).exists():
			message= 'User Already Exist'
			return render(request,'registration.html', {'message':message})

		else:
			u='A00'
			x=1
			uid=u+str(x)
			while agent_account.objects.filter(agent_id=uid):
				x=x+1
				uid=u+str(x)
			x=int(x)
			try:
				subject='mail from RealEstate'
				msg= ''' Hello sir,

		You are successfully registered, but your account is not active
		please wait for the owner response 

		Thanks & Regards
		Real Estate''' 
				

				email = EmailMessage(subject, msg, to=[e])
				email.send()

				try:
					print('esle')
					sus='New Agent Register'
					mess= ''' Hello sir,
		This Person want to make your agent
		detail of the person is here

				'''+"Name :" +n+('\n')+"Gender :" +g+('\n')+"Mail ID :"+e+('\n')+"Phone no. :"+ph+('\n')+"Address :"+ad+('\n')+"City :"+c+('\n')+"Aadhar card no. :" +aa+'''

				Thanks & Regards
				Real Estate''' 


			
					email = EmailMessage(sus, mess, to=['testm1214@gmail.com'])
					email.send()
					sv=agent_account(agent_id=uid, name=n, gender=g, email=e, address=ad, city=c, phone=ph, aadhar=aa, password=p, status=status)
					sv.save()
					message='You are successfully registered.'	
					return render(request,'registration.html', {'message':message})
				except Exception:
						message='Fill The form again'	
						return render(request,'registration.html', {'message':message})
			except Exception:
				message=' enter valid mail address'
				return render(request,'registration.html', {'message':message})


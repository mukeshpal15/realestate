from django.core.paginator import *
from django.shortcuts import render, redirect
from django.conf import  settings
from realstateapp.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from realstateapp.form import *
from .models import * 
from django.contrib.auth import logout
from django.core.mail import EmailMessage
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages

import uuid
import string
from realstateapp.realutil import *

def error(request):
	#obj=PropertyData.objects.all().delete()
	#obj=PropertyImagesData.objects.all().delete()
	return render(request,'Error.html',{})

def index(request):
	dic={'cdata':GetPropertyCategoryData()}
	return render(request, 'index.html',dic)

def properties(request):
	return render(request, 'properties.html', {})

def blog(request):
	return render(request, 'blog.html', {})
def about(request):
	b=0
	t=0
	if request.session.has_key('user_id'):
		b=1
		t=1
		return render(request, 'about.html', {'b':b, 't':t})
	else:
		return render(request, 'login.html', {})
def property_detail(request):
	return render(request, 'property-details.html', {})
def contact(request):
	return render(request, 'contact.html', {})
def registration(request):
	return render(request, 'registration.html', {})
def login(request):
	return render(request, 'login.html', {})
def adminlogin(request):
	return render(request, 'adminlogin.html', {})
def agent_forgot_pass(request):
	return render(request, 'agentforget.html', {})
def userregistation(request):
	return render(request, 'userregistation.html',{})
def loginformuser(request):
	return render(request, 'userlogin.html',{})
def user_forgot_pass(request):
	return render(request, 'userforgot.html', {})
@csrf_exempt
def adminlogincheck(request):
	if request.method=="POST":
		e=request.POST.get('email')
		p=request.POST.get('pass')
		if e=="admin@homespace.com" and p=="1234":
			return render(request, 'adminpannel.html', {})
		else:
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Login Failed'
			return render(request, 'adminlogin.html', {'alert':alert})
@csrf_exempt
def agentdata(request):
	s='active'
	u= 'not active'
	agent=agent_account.objects.filter(status=s)
	notagent=agent_account.objects.filter(status=u)
	return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
@csrf_exempt
def make_active_agent(request):
	if request.method=="POST":
		s='active'
		u= 'not active'
		m= request.POST.get('set')
		if agent_account.objects.filter(agent_id=m):
			t=agent_account.objects.filter(agent_id=m)
			for i in t:
				i.status=s
				i.save()
		agent=agent_account.objects.filter(status=s)
		notagent=agent_account.objects.filter(status=u)
		return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
@csrf_exempt
def make_deactive_agent(request):
	if request.method=="POST":
		s='active'
		u= 'not active'
		m= request.POST.get('set')
		if agent_account.objects.filter(agent_id=m):
			t=agent_account.objects.filter(agent_id=m)
			for i in t:
				i.status=u
				i.save()
		agent=agent_account.objects.filter(status=s)
		notagent=agent_account.objects.filter(status=u)
		return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
@csrf_exempt
def openaddproperty(request):
	if request.method=="POST":
		obj=PropertyCategoryData.objects.all()
		lt=[]
		for x in obj:
			lt.append(x.Category_Name)
		dic={'category':lt,
			'pdata':GetAllPropertyData()}
		return render(request, "addproperty.html",dic)
	else:
		return redirect('/error/')
@csrf_exempt
def openaddpropertycategory(request):
	if request.method=="POST":
		return render(request, "addpropertycategory.html",{})

@csrf_exempt
def savepropertycategory(request):
	if request.method=="POST":
		form=ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
				m=form.cleaned_data['image']
				p="C00"
				x=1
				pid=p+str(x)
				while PropertyCategoryData.objects.filter(Category_ID=pid).exists():
					x=x+1
					pid=p+str(x)
				x=int(x)
				n=request.POST.get('name')
				obj=PropertyCategoryData(
					Category_ID=pid,
					Category_Name=n,
					Category_Image=m,
					)
				obj.save()
				b1='''<script type="text/javascript">
				alert("'''
				b2='''");</script>'''
				alert=b1+'Saved'+b2
				return render(request, "addpropertycategory.html",{'alert':alert})

	else:
		return redirect('/error/')

@csrf_exempt
def saveproperty(request):
	if request.method=="POST":
		n=request.POST.get('name')
		a=request.POST.get('about')
		property_price=request.POST.get('price')
		c=request.POST.get('category')
		y=request.POST.get('builtyear')
		ad=request.POST.get('address')
		ar=request.POST.get('area')
		bd=request.POST.get('beds')
		bt=request.POST.get('baths')
		gr=request.POST.get('garages')
		p="P00"
		x=1
		pid=p+str(x)
		while PropertyData.objects.filter(Property_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		obj=PropertyData(
			Property_ID=pid,
			Property_Name=n,
			Property_About=a,
			Property_Address=ad,
			Property_Area=ar,
			Property_Beds=bd,
			Property_Baths=bt,
			Property_Garages=gr,
			Property_Price=property_price,
			Property_Category=c,
			Property_BuiltYear=y
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request, 'adminpannel.html', {'alert':alert,'pdata':GetAllPropertyData()})
	else:
		return redirect('/error/')

def agent_signup(request):
	if request.method=="POST":
		n= request.POST.get('name')
		g= request.POST.get('gender')
		e= request.POST.get('email')
		ad= request.POST.get('address')
		c = request.POST.get('city')
		ph= request.POST.get('phone')
		aa=request.POST.get('aadhar')
		u= 'not active'
		status=u
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

@csrf_exempt
def openaddpropertycategory(request):
	if request.method=="POST":
		return render(request, "addpropertycategory.html",{'cdata':GetPropertyCategoryData()})
	else:
		return redirect('/error/')

@csrf_exempt
def openaddpropertyimages(request):
	if request.method=="POST":
		dic={'propertyid':GetPropertyID(),
			'propertyimagedata':GetPropertyImageData()}
		return render(request, "addpropertyimages.html",dic)
	else:
		return redirect('/error/')

@csrf_exempt
def savepropertyimages(request):
	if request.method=="POST":
		n=request.POST.get('propertyid')
		form=ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			m=form.cleaned_data['image']
			obj=PropertyImagesData(
				Property_ID=n,
				Property_Image=m
				)
			obj.save()
			dic={'propertyid':GetPropertyID(),
				'propertyimagedata':GetPropertyImageData()}
			return render(request, "addpropertyimages.html",dic)
	else:
		return redirect('/error/')

<<<<<<< HEAD
@csrf_exempt
def openpropertycategory(request):
		category=request.GET.get('cname')
		request.session['cname'] = category
		page = request.GET.get('page')
		cdata=[]
		paginator = Paginator(GetPropertyThumbData(category), 15)
		try:
			cdata = paginator.page(page)
		except PageNotAnInteger:
			cdata = paginator.page(1)
		except EmptyPage:
			cdata = paginator.page(paginator.num_pages)
		dic={'cdata':cdata,
			'category':category}
		return render(request,"propertycategories.html",dic)
def propertypaginator(request):
	page = request.GET.get('page')
	cdata=[]
	paginator = Paginator(GetPropertyThumbData(request.session['cname']), 15)
	try:
		cdata = paginator.page(page)
	except PageNotAnInteger:
		cdata = paginator.page(1)
	except EmptyPage:
		cdata = paginator.page(paginator.num_pages)
	dic={'cdata':cdata,
		'category':request.session['cname']}
	return render(request,"propertycategories.html",dic)
def openmyaccount(request):
	return render(request,"myaccount.html",{})
=======
def user_signup(request):
	if request.method=="POST":
		n= request.POST.get('name')
		g= request.POST.get('gender')
		e= request.POST.get('email')
		ad= request.POST.get('address')
		c = request.POST.get('city')
		ph= request.POST.get('phone')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]

		if user_account.objects.filter(email=e).exists():
			message= 'User Already Exist'
			return render(request,'userregistation.html',{'message':message})

		elif user_account.objects.filter(phone=ph).exists():
			message= 'User Already Exist'
			return render(request,'userregistation.html', {'message':message})

		else:
			u='U00'
			x=1
			uid=u+str(x)
			while user_account.objects.filter(user_id=uid):
				x=x+1
				uid=u+str(x)
			x=int(x)
			try:
				subject='mail from RealEstate'
				msg= ''' Hello sir,

		You are successfully registered, 
		your password is :'''+p+''' 

		Thanks & Regards
		Real Estate''' 
				

				email = EmailMessage(subject, msg, to=[e])
				email.send()
				sv=user_account(user_id=uid, name=n, gender=g, email=e, address=ad, city=c, phone=ph,password=p)
				sv.save()
				message='You are successfully registered. password is send to your given mail account'	
				return render(request,'userregistation.html', {'message':message})
			except Exception:
				message=' enter valid mail address'
				return render(request,'userregistation.html', {'message':message})
@csrf_exempt
def user_login(request):
	if request.method=="POST":
		b=0
		h=0
		e=request.POST.get('email')
		p=request.POST.get('password')
		ua = user_account.objects.all()
		for elt in ua:
			if elt.email==e and elt.password==p:
				for i in ua:
					b=1
					userid=i.user_id
					request.session['user_id'] = userid
					break
				print('go')
		if request.session.has_key('user_id') and b==1: 
			h=1
			return render(request, 'index.html', {'b':b, 'h': h})
		else:
			print('helo')
			message='Please Enter valid details'
			return render(request,'userlogin.html',{'message': message})


@csrf_exempt
def password_send_to_user(request):
	if request.method=="POST":
		e=request.POST.get('email')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		if user_account.objects.filter(email=e).exists():
			u=user_account.objects.filter(email=e)
			for i in u:
				i.password=p
				break
			subject='mail from RealEstate'
			msg= ''' Hello sir,

			Your passwaord has been changed, 
			your password is :'''+p+''' 

			Thanks & Regards
			Real Estate''' 
					
			try:
				email = EmailMessage(subject, msg, to=[e])
				email.send()
				i.save()
				return HttpResponse("<script> alert('Hello User, Your password has been sent to your registered Email. If you have not received the password, go to the contact page and send an email. Will be processed within 24 hours !!'); window.location.replace('/loginformuser/') </script>")
			except Exception:
				return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/user_forgot_pass/') </script>")
		else:
			return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/user_forgot_pass/') </script>")

@csrf_exempt
def password_send_to_agent(request):
	if request.method=="POST":
		e=request.POST.get('email')
		randomString = uuid.uuid4().hex
		p= randomString.lower()[0:8]
		if agent_account.objects.filter(email=e).exists():
			u=agent_account.objects.filter(email=e)
			for i in u:
				i.password=p
				break
			subject='mail from RealEstate'
			msg= ''' Hello sir,

			Your passwaord has been changed, 
			your password is :'''+p+''' 

			Thanks & Regards
			Real Estate''' 
					
			try:
				email = EmailMessage(subject, msg, to=[e])
				email.send()
				i.save()
				return HttpResponse("<script> alert('Hello Agent, Your password has been sent to your registered Email. If you have not received the password, go to the contact page and send an email. Will be processed within 24 hours !!'); window.location.replace('/login/') </script>")
			except Exception:
				return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/agent_forgot_pass/') </script>")
		else:
			return HttpResponse("<script> alert('Please Enter The Registered Email Address .!!'); window.location.replace('/agent_forgot_pass/') </script>")

def send_mail_by_contact(request):
	if request.method=="POST":
		n= request.POST.get('name')
		e= request.POST.get('email')
		s= request.POST.get('subject')
		m= request.POST.get('message')
		subject='mail from RealEstate'
		msg= ''' Hello sir,

	Someone contact you, 
	details are given below 
'''+"Name :" +n+('\n')+"Mail ID :"+e+('\n')+"Subject :"+s+('\n')+"Message :"+m+'''

	Thanks & Regards
	Real Estate''' 

		email = EmailMessage(subject, msg, to=['testm1214@gmail.com'])
		email.send()
		print('heloo')
		return HttpResponse("<script> alert('Hello sir, your message has been sent. Will be processed within 24 hours !!'); window.location.replace('/contact/') </script>")
<<<<<<< HEAD





@csrf_exempt
def Log(request):

	try:
	    if request.session.has_key('user_id'):
	     	request.session.flush()
	     	del request.session['user_id']
	     	logout(request)
	     	
	     	return HttpResponse("<script> window.location.replace('/login/'); </script>")
	except:
 		return HttpResponse("<script> window.location.replace('/login/'); </script>")
=======
>>>>>>> b8b165508040b34db5dd91cb1ee7e2ede941495f
>>>>>>> 66d3abf3b794a02a06ea16fa73fbb6f7480f0a6c

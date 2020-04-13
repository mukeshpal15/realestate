from django.core.paginator import *
from django.shortcuts import render, redirect
from django.conf import  settings
from realstateapp.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
#from realstateapp.form import *
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
	b=0
	h=0
	obj=agent_account.objects.all()
	dic=allblogs()[0:3]

	try:
		try:	
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				return render(request, 'index.html',{'obj': obj, 'b':b, 'h':h, 'elt':dic})
			else:
				b=1
				dic={'obj': obj, 'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				return render(request, 'index.html',dic)
			
		except:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				dic={'obj':obj,'b':b, 'h':h}
				dic.update({'cdata':GetPropertyCategoryData()})
				return render(request, 'index.html',{'obj': obj, 'b':b, 'h':h, 'elt':dic})
			else:
				return render(request, 'index.html',{'obj': obj,'elt':dic})
	
	except Exception:
		dic={'obj': obj}
		dic.update({'cdata':GetPropertyCategoryData()})
		return render(request, 'index.html',{'obj': obj,})


		
	
def properties(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'properties.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'properties.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'properties.html',{'obj': obj, 'b':b, 'h':h})
			else:
				return render(request, 'properties.html',{'obj': obj,})
	except Exception:
		return render(request, 'properties.html',{'obj': obj,})	

def blog(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	dic=allblogs()
	try:	
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'blog.html',{'obj': obj, 'b':b, 'h':h,'elt':dic})
			else:
				b=1
				return render(request, 'blog.html',{'obj': obj, 'elt':dic})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'blog.html',{'obj': obj, 'b':b, 'h':h, 'elt':dic})
			else:
				return render(request, 'blog.html',{'obj': obj, 'elt':dic})
	except Exception:
		
		return render(request, 'blog.html',{'obj': obj, 'elt':dic})

def about(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'about.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'about.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'about.html',{'obj': obj, 'b':b, 'h':h})
			else:
				return render(request, 'about.html',{'obj': obj,})
	except Exception:
		return render(request, 'about.html',{'obj': obj,})

def property_detail(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'property-details.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'property-details.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'property-details.html',{'obj': obj, 'b':b, 'h':h})
			else:
				return render(request, 'property-details.html',{'obj': obj,})
	except Exception:
		return render(request, 'property-details.html',{'obj': obj,'elt':allblogs()})

	
def contact(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			if user_account.objects.filter(user_id=n).get():
				b=1
				h=0
				return render(request, 'contact.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'contact.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			if agent_account.objects.filter(agent_id=a).get():
				b=1
				h=0
				return render(request, 'contact.html',{'obj': obj, 'b':b, 'h':h})
			else:
				return render(request, 'contact.html',{'obj': obj,})
	except Exception:
		return render(request, 'contact.html',{'obj': obj,})

	
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
	if request.method=="POST":
		s='active'
		u= 'not active'
		agent=agent_account.objects.filter(status=s)
		notagent=agent_account.objects.filter(status=u)
		return render(request, 'agentsdata.html', {'active': agent, 'deactive': notagent})
	else:
		return redirect('/error/')

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
		return render(request, "addpropertycategory.html",{'cdata':GetPropertyCategoryData()})

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
				return render(request, "addpropertycategory.html",{'alert':alert,'cdata':GetPropertyCategoryData()})

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
@csrf_exempt
def agent_signup(request):
	if request.method=="POST":
		
		n= request.POST.get('name')
		g= request.POST.get('gender')
		e= request.POST.get('email')
		ad= request.POST.get('address')
		c = request.POST.get('city')
		ph= request.POST.get('phone')
		aa=request.POST.get('aadhar')
		fb=request.POST.get('facebook')
		tw=request.POST.get('twitter')
		LI=request.POST.get('linkedin')
		m=request.FILES['pic']
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
				subject='Mail From Shri Raj Property'
				msg= ''' Hello sir,

		You are successfully registered, but your account is not active
		please wait for the owner response 

		Thanks & Regards
		Shri Raj Property''' 
				

				email = EmailMessage(subject, msg, to=[e])
				email.send()
				try:
					sus='New Agent Register'
					mess= ''' Hello sir,
		This Person want to make your agent
		detail of the person is here

				'''+"Name :" +n+('\n')+"Gender :" +g+('\n')+"Mail ID :"+e+('\n')+"Phone no. :"+ph+('\n')+"Address :"+ad+('\n')+"City :"+c+('\n')+"Aadhar card no. :" +aa+"Facebook link :"+fb+('\n')+"linkedIn link :"+LI+('\n')+"Twitter link. :"+tw +'''

				Thanks & Regards
				Shri Raj Property''' 


			
					email = EmailMessage(sus, mess, to=['testm1214@gmail.com'])
					email.send()
					sv=agent_account(agent_id=uid,
									name=n,
									gender=g,
									email=e,
									address=ad,
									city=c,
									phone=ph,
									aadhar=aa,
									password=p,
									facebook=fb,
									twitter=tw,
									linkedin=LI,
									status=status,
									agentpic=m
									  )
					sv.save()
					message='You are successfully registered.'	
					return render(request,'registration.html', {'message':message})
				except Exception:
					message='Fill The Form Again'	
					return render(request,'registration.html', {'message':message})
			except Exception:
				message=' Enter Valid Mail Address'
				return render(request,'registration.html', {'message':message})
	else:
		message=' Enter Valid Mail Address'
		return render(request,'registration.html', {'message':message})

def dele(request):
	obj=agent_account.objects.all()
	obj.delete()
	return render(request, 'index.html',{})


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
		dic.update({'catedata':GetPropertyCategoryData()})
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
	dic.update({'catedata':GetPropertyCategoryData()})
	return render(request,"propertycategories.html",dic)
def openmyaccount(request):
	return render(request,"myaccount.html",{})

def openchangeaccountdetails(request):
	uid=request.session['user_id']
	dic=GetUserData2(uid)
	return render(request,"changeaccountdetails.html",dic)

@csrf_exempt
def savechangeaccountdetails(request):
	if request.method=="POST":
		uid=request.session['user_id']
		obj=user_account.objects.filter(user_id=uid)
		obj.update(address=request.POST.get('address'))
		obj.update(city=request.POST.get('city'))
		obj.update(phone=request.POST.get('phone'))
		dic=GetUserData2(uid)
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved successfully'+b2
		dic.update({'alert':alert})
		return render(request,"myaccount.html",dic)


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
				subject='Mail From Shri Raj Property'
				msg= ''' Hello sir,

		You are successfully registered, 
		your password is :'''+p+''' 

		Thanks & Regards
		Shri Raj Property''' 
				

				email = EmailMessage(subject, msg, to=[e])
				email.send()
				sv=user_account(user_id=uid, name=n, gender=g, email=e, address=ad, city=c, phone=ph,password=p)
				sv.save()
				message='You are successfully registered. password is send to your given mail account'	
				return render(request,'userregistation.html', {'message':message})
			except Exception:
				message='Enter Valid Mail Address'
				return render(request,'userregistation.html', {'message':message})
@csrf_exempt
def user_login(request):
	if request.method=="POST":
		b=0
		h=0
		e=request.POST.get('email')
		p=request.POST.get('password')
		ua = user_account.objects.filter(email=e)
		if user_account.objects.filter(email=e, password=p).exists:
			for i in ua:
				c=i.user_id
				request.session['user_id']=c
				b=1
				break
		if request.session.has_key('user_id') and b==1: 
			h=1
			dic=GetUserData(e)
			return render(request,"myaccount.html",dic)
		else:
			message='Please Enter Valid Details'

			return render(request,'userlogin.html',{'message': message})
@csrf_exempt
def agent_login(request):
	b=0
	h=0
	s='active'
	e=request.POST.get('email')
	p=request.POST.get('pass')
	ua = agent_account.objects.filter(email=e)
	if agent_account.objects.filter(email=e, password=p).exists():
		if agent_account.objects.filter(status=s).exists():
			for i in ua:
				c=i.agent_id
				request.session['agent_id']=c
				b=1
				break

		else:
			message='Your account is not activated'
			return render(request,'login.html',{'message': message})

		if request.session.has_key('agent_id') and b==1: 
			h=1
			dic=getagentinfo(request.session['agent_id'])
			dic.update({'blogs':getblogs(request.session['agent_id'])})
			return render(request, 'agentdesk.html', dic)
	else:
		message='Please Enter valid details'
		return render(request,'login.html',{'message': message})

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
			subject='Mail From Shri Raj Property'
			msg= ''' Hello sir,

			Your passwaord has been changed, 
			your password is :'''+p+''' 

			Thanks & Regards
			Shri Raj Property''' 
					
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
			subject='Mail From Shri Raj Property'
			msg= ''' Hello sir,

			Your passwaord has been changed, 
			your password is :'''+p+''' 

			Thanks & Regards
			Shri Raj Property''' 
					
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
		subject='Mail From Shri Raj Property'

		msg= ''' Hello sir,

	Someone contact you, 
	details are given below 
'''+"Name :" +n+('\n')+"Mail ID :"+e+('\n')+"Subject :"+s+('\n')+"Message :"+m+'''

	Thanks & Regards
	Shri Raj Property''' 

		email = EmailMessage(subject, msg, to=['testm1214@gmail.com'])
		email.send()
		return HttpResponse("<script> alert('Hello sir, your message has been sent. Will be processed within 24 hours !!'); window.location.replace('/contact/') </script>")

def openmyaccount(request):
	return render(request,"myaccount.html",{})





@csrf_exempt
def Log(request):
	b=0
	h=0
	obj=agent_account.objects.all()
	try:
		try:
			n=request.session['user_id']
			del request.session['user_id']
			request.session.flush()
			if user_account.objects.filter(user_id=request.session['user_id']).get():
				b=1
				h=0
				return render(request, 'index.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'index.html',{'obj': obj,})
		except Exception:
			a=request.session['agent_id']
			del request.session['agent_id']
			request.session.flush()
			if agent_account.objects.filter(agent_id=request.session['agent_id']).get():
				b=1
				h=0
				return render(request, 'index.html',{'obj': obj, 'b':b, 'h':h})
			else:
				b=1
				return render(request, 'index.html',{'obj': obj,})
	except Exception:
		return render(request, 'index.html',{'obj': obj,})

			
	
def agentblog(request):
	agentid=request.session['agent_id']
	dic=getagentinfo(agentid)
	dic.update({'blogs':getblogs(agentid)})
	return render(request, 'agentdesk.html', dic)
	
 		

@csrf_exempt
def openproperty(request):
	pid=request.GET.get('pid')
	dic=GetPropertyData(pid)
	dic.update({'catedata':GetPropertyCategoryData()})
	return render(request,'property-details.html',dic)
@csrf_exempt
def blog_page(request):
	return render(request, 'enterblog.html',{})

@csrf_exempt
def post_blog(request):
	if request.method=="POST":
		n=request.POST.get('subject')
		p=request.FILES['pic']
		m=request.POST.get('mess')
		u='U00'
		x=1
		uid=u+str(x)
		while blog_table.objects.filter(blog_no=uid):
			x=x+1
			uid=u+str(x)
		x=int(x)
		try:
			if agent_account.objects.filter(agent_id=request.session['agent_id']).get():
				sv=blog_table(
					agent_id=request.session['agent_id'],
					blog_no=uid,
					pic_of_pro=p,
					subject=n,
					Desc=m
					)
				sv.save()
				return HttpResponse("<script> alert('Your Blog Is Posted !!'); window.location.replace('/blog_page/') </script>")
		except Exception:
			obj=PropertyCategoryData.objects.all()
			lt=[]
			for x in obj:
				lt.append(x.Category_Name)
			dic={'category':lt,
			'pdata':GetAllPropertyData()}
			
			sv=blog_table(
				agent_id='admin',
				blog_no=uid,
				pic_of_pro=p,
				subject=n,
				Desc=m
				)
			sv.save()
			return HttpResponse("<script> alert('Your Blog Is Posted !!'); window.location.replace('/blog_page/') </script>")

def openmyblogs(request):
	return render(request,'myblogs.html',{})
	return HttpResponse("<script> alert('Your Blog Is Posted !!'); window.location.replace('/adminlogin/') </script>")
def openmyblogs(request):
	return render(request,'myblogs.html',{})

def openuseraccount(request):
	try:

		uid=request.session['user_id']
		dic=GetUserData2(uid)	
		return render(request,"myaccount.html",dic)
	except Exception:
		uid=request.session['agent_id']
		dic=getagentinfo(uid)
		return render(request,'myaccount.html', dic)

@csrf_exempt
def changeuserpassword(request):
	if request.method=="POST":
		uid=request.session['user_id']
		op=request.POST.get('old')
		np=request.POST.get('new')
		obj=user_account.objects.filter(password=op,user_id=uid)
		obj.update(password=np)
		if user_account.objects.filter(password=np,user_id=uid).exists():
			dic=GetUserData2(uid)
			email=''
			obj=user_account.objects.filter(user_id=uid)
			for x in obj:
				email=x.email
				break
			subject='Alert! : Your Account Password Has Changed'
			msg= '''Hi there!
Your account password has been change from '''+op+''' to '''+np+'''.
If this was not you please report us.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
			e.send()
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Password Changed Successfully'+b2
			dic.update({'alert':alert})		
			return render(request,"myaccount.html",dic)
		else:
			dic=GetUserData2(uid)
			b1='''<script type="text/javascript">
			alert("'''
			b2='''");</script>'''
			alert=b1+'Incorrect Password'+b2
			dic.update({'alert':alert})
			email=''
			obj=user_account.objects.filter(user_id=uid)
			for x in obj:
				email=x.email
				break
			subject='Alert! : Someone tries to change your Pssword'
			msg= '''Hi there!
Someone tries to change your Pssword. Kindly login and change your password again.

Thanks & Regards
Shri Raj Property'''
			e = EmailMessage(subject, msg, to=[email])
			e.send()
			return render(request,"myaccount.html",dic)
def openuserorder(request):
	return render(request,'myorders.html',{})


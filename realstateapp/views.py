from django.shortcuts import render
from django.conf import  settings
from realstateapp.models import *
from django.views.decorators.csrf import csrf_exempt
from realstateapp.form import *

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
def adminlogin(request):
	return render(request, 'adminlogin.html', {})
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
def openaddproperty(request):
	if request.method=="POST":
		obj=PropertyCategoryData.objects.all()
		lt=[]
		for x in obj:
			lt.append(x.Category_Name)
		dic={'category':lt}
		return render(request, "addproperty.html",dic)
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

	b1='''<script type="text/javascript">
	alert("'''
	b2='''");</script>'''
	alert=b1+'Error'+b2
	return render(request, "addpropertycategory.html",{'alert':alert})

@csrf_exempt
def saveproperty(request):
	if request.method=="POST":
		n=request.POST.get('name')
		a=request.POST.get('about')
		p=request.POST.get('price')
		c=request.POST.get('category')
		y=request.POST.get('builtyear')
		p="P00"
		x=1
		pid=p+str(x)
		while PropertyCategoryData.objects.filter(Category_ID=pid).exists():
			x=x+1
			pid=p+str(x)
		x=int(x)
		obj=PropertyData(
			Property_ID=pid,
			Property_Name=n,
			Property_About=a,
			Property_Price=p,
			Property_Category=c,
			Property_BuiltYear=y
			)
		obj.save()
		b1='''<script type="text/javascript">
		alert("'''
		b2='''");</script>'''
		alert=b1+'Saved'+b2
		return render(request, 'adminpannel.html', {'alert':alert})
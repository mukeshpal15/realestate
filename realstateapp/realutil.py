from realstateapp.models import *

def GetPropertyID():
	obj=PropertyData.objects.all()
	lt=[]
	dic={}
	for x in obj:
		dic={'ID':x.Property_ID,
			'Name':x.Property_Name}
		lt.append(dic)
	return lt
def GetPropertyName(pid):
	obj=PropertyData.objects.filter(Property_ID=pid)
	n=''
	for x in obj:
		n=x.Property_Name
	return n
def GetPropertyImageCount(pid):
	obj=PropertyImagesData.objects.filter(Property_ID=pid)
	count=0
	for x in obj:
		count=count+1
	return str(count)
def GetPropertyImageData():
	obj=PropertyImagesData.objects.all()
	lt=[]
	dic={}
	pid=[]
	pname=[]
	pcount=[]
	for x in obj:
		pid.append(x.Property_ID)
	for x in obj:
		pname.append(GetPropertyName(x.Property_ID))
	for x in obj:
		pcount.append(GetPropertyImageCount(x.Property_ID))
		
	pid=list(set(pid))
	pname=list(set(pname))
	pcount=list(set(pcount))
	for (a,b,c) in zip(pid,pname,pcount):
		dic={'property_id':a,
			'property_name':b,
			'image_count':c}
		lt.append(dic)
	return lt
def GetPropertyCategoryData():
	obj=PropertyCategoryData.objects.all()
	dic={}
	lt=[]
	for x in obj:
		dic={'cid':x.Category_ID,
			'cname':x.Category_Name,
			'cimage':x.Category_Image.url}
		lt.append(dic)
	return lt
def GetAllPropertyData():
	obj=PropertyData.objects.all()
	dic={}
	lt=[]
	for x in obj:
		dic={'pid':x.Property_ID,
			'pname':x.Property_Name,
			'pprice':x.Property_Price,
			'pcategory':x.Property_Category,
			'pyear':x.Property_BuiltYear}
		lt.append(dic)
	return lt
def getuserinfo(user_id):
	dic={}
	obj=user_account.objects.filter(user_id=user_id)
	for i in obj:
		dic={
			'name': i.name
		}
		break
	return dic
def GetPropertyThumbData(category):
	obj=PropertyData.objects.filter(Property_Category=category)
	dic={}
	lt=[]
	for x in obj:
		dic={
		'id':x.Property_ID,
		'name':x.Property_Name,
		'price':x.Property_Price,
		'address':x.Property_Address,
		'area':x.Property_Area,
		'beds':x.Property_Beds,
		'baths':x.Property_Baths,
		'garages':x.Property_Garages
		}
		obj1=PropertyImagesData.objects.filter(Property_ID=x.Property_ID)
		for y in obj1:
			dic.update({'image':y.Property_Image.url})
			break
		lt.append(dic)
	return lt

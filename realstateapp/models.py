from django.db import models

class PropertyCategoryData(models.Model):
	Category_ID=models.CharField(max_length=100)
	Category_Name=models.CharField(max_length=50)
	Category_Image=models.ImageField(upload_to="categoryimages/")
	class Meta:
		db_table="PropertyCategoryData"

class PropertyData(models.Model):
	Property_ID=models.CharField(max_length=100)
	Property_Name=models.CharField(max_length=100)
	Property_About=models.CharField(max_length=1000)
	Property_Price=models.CharField(max_length=50)
	Property_Category=models.CharField(max_length=100)
	Property_BuiltYear=models.CharField(max_length=50)
	class Meta:
		db_table="PropertyData"

class agent_account(models.Model):
	agent_id=models.CharField(max_length=20)
	name=models.CharField(max_length=40)
	gender=models.CharField(max_length=10)
	email=models.CharField(max_length=50)
	address=models.CharField(max_length=400)
	city=models.CharField(max_length=20)
	phone=models.CharField(max_length=15)
	aadhar=models.CharField(max_length=16)
	password=models.CharField(max_length=40)
	status = models.CharField(max_length=5)
	class Meta:
		db_table="agent_account"

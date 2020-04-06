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
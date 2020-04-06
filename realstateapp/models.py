from django.db import models

# Create your models here.
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
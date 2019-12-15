from django.db import models
from datetime import datetime 
import os 
import random

# Create your models here.

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext 

def upload_image_path(instance, filename):
	new_file_name = random.randint(1,983127831)
	name, ext = get_filename_ext(filename)
	final_name = '{new_file_name}{ext}'.format(new_file_name=new_file_name, ext=ext)
	return 'products/{new_file_name}/{final_name}'.format(new_file_name=new_file_name,final_name=final_name)


class Category(models.Model):
	title = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='categories/%Y/%m',blank=True)
	date_created = models.DateTimeField(default=datetime.now, blank=True)
	date_updated = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.title 

class Product(models.Model):
	title 		 = models.CharField(max_length=100)
	description  = models.TextField()
	price 		 = models.DecimalField(max_digits=10, decimal_places=2)
	old_price 	 = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
	image 		 = models.ImageField(upload_to=upload_image_path, blank=True)
	date_created = models.DateTimeField(default=datetime.now, blank=True)
	date_updated = models.DateTimeField(default=datetime.now, blank=True)
	category  	 = models.ForeignKey(Category, on_delete=models.CASCADE)
	featured	 = models.BooleanField(default=False)
	bestseller   = models.BooleanField(default=False)



	def __str__(self):
		return self.title
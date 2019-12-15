from django.db import models
from datetime import datetime 
import os 
import random
# Create your models here.

#  Upload Image 
def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext 

def upload_image_path(instance, filename):
	new_file_name = random.randint(1,983127831)
	name, ext = get_filename_ext(filename)
	final_name = '{new_file_name}{ext}'.format(new_file_name=new_file_name, ext=ext)
	return 'blog/{new_file_name}/{final_name}'.format(new_file_name=new_file_name,final_name=final_name)


class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	image = models.ImageField(upload_to=upload_image_path)
	img_1 = models.ImageField(upload_to=upload_image_path, blank=True)
	img_2 = models.ImageField(upload_to=upload_image_path, blank=True)
	description = models.TextField()
	is_published = models.BooleanField(default=True)

	def __str__(self):
		return self.title 

class Comment(models.Model):
	name = models.CharField(max_length=100)
	comment = models.TextField()
	email = models.EmailField()
	time = models.DateTimeField(default=datetime.now,blank=True)
	image = models.ImageField(null=True, default='images/comment/3.png')
	is_published = models.BooleanField(default=True)
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

	def __str__(self):
		return self.name 
	

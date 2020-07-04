from django.db import models
from datetime import datetime    

# Create your models here.
TYPE_CHOICES = [
    ('Remote Fulltime ', 'Remote Fulltime '),
    ('Remote part-time ', 'Remote part-time '),
    ('Fulltime on site ', 'Fulltime On site '),
    ('Part time on site', 'Part-time On site '),
]
class Category(models.Model):
	name=models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Opening(models.Model):
	title=models.CharField(max_length=100)
	category=models.ManyToManyField('Category', related_name='jobs')
	description=models.TextField() 
	requirements=models.TextField() 
	location=models.CharField(max_length=100)
	type=models.CharField(max_length=20, choices=TYPE_CHOICES) 
	date_line=models.DateTimeField
	
	
	def __str__(self):
		return self.title
		
class Patners(models.Model):
	name=models.CharField(max_length =150) 
	
	def __str__(self):
		return self.name
		
		
	

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
	class Meta:
		verbose_name_plural="Categories"
	def __str__(self):
		return self.name

class Opening(models.Model):
	title=models.CharField(max_length=100)
	recruiter=models.CharField(max_length=50)
	recruiter_email=models.EmailField(max_length=50)
	category=models.ManyToManyField('Category', related_name='jobs')
	description=models.TextField()
	location=models.CharField(max_length=100)
	type=models.CharField(max_length=20, choices=TYPE_CHOICES)
	date_line=models.DateTimeField()
	created=models.DateTimeField(auto_now_add=True)
	salary=models.PositiveIntegerField()
	qualification_1=models.CharField(max_length=300)
	qualification_2=models.CharField(max_length=300)
	qualification_3=models.CharField(max_length=300)
	qualification_4=models.CharField(max_length=300)
	qualification_5=models.CharField(max_length=300)
	benefit_1=models.CharField(max_length=300)
	benefit_2=models.CharField(max_length=300)
	benefit_3=models.CharField(max_length=300)
	benefit_4=models.CharField(max_length=300)
	benefit_5=models.CharField(max_length=300)
	role_1=models.CharField(max_length=300)
	role_2=models.CharField(max_length=300)
	role_3=models.CharField(max_length=300)
	role_4=models.CharField(max_length=300)
	role_5=models.CharField(max_length=300)

	def __str__(self):
		return self.title
		
class Patner(models.Model):
	name=models.CharField(max_length =150)
	logo=models.FileField(upload_to="patners/%Y/%m/%d")
	def __str__(self):
		return self.name

class Talent(models.Model):
	name=models.CharField(max_length=60)
	title=models.CharField(max_length=60)
	image=models.ImageField(upload_to="talents/%Y/%m/%d")
	def __str__(self):
		return self.name

class Testimony(models.Model):
	name=models.CharField(max_length=60)
	body=models.TextField()
	class Meta:
		verbose_name_plural="Testimonies"
	def __str__(self):
		return self.name

class Resume(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	
class Application(models.Model):
  opening = models.CharField(max_length=200)
  opening_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  website = models.CharField(max_length=100)
  resume = models.FileField(upload_to='applications/%Y/%m/%d')
  cover_letter = models.TextField(blank=True)
  application_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name


		
		
	

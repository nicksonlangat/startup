from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	categories=Category.objects.all()
	openings=Opening.objects.all()
	patners=Patner.objects.all()
	talents=Talent.objects.all()
	testimonies=Testimony.objects.all()
	context ={
	"categories" : categories, 
	"openings" :openings, 
	"patners" :patners,
	"talents":talents,
	"testimonies":testimonies
	}
	return render(request, "index.html", context) 

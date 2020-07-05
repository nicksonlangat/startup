from django.shortcuts import render
from .models import Category, Opening, Patner

# Create your views here.
def index(request):
	categories=Category.objects.all()
	openings=Opening.objects.all()
	patners=Patner.objects.all()
	context ={
	"categories" : categories, 
	"openings" :openings, 
	"patners" :patners
	
	}
	return render(request, "index.html", context) 

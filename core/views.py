from django.shortcuts import render
from .models import Category, Opening, Patners

# Create your views here.
def index(request):
	categories=Category.objects.all()
	openings=Opening.objects.all()
	patners=Patners.objects.all()
	context ={
	"categories" : categories, 
	"openings" :openings, 
	"patners" :patners
	
	}
	return render(request, "index.html", context) 

from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import ResumeForm

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

def detail(request, opening_id):
    opening = get_object_or_404(Opening, pk=opening_id)
    return render(request, 'detail.html', {'opening':opening})

def resume(request):
    # Handle file upload
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Resume(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('home')
    else:
        form = ResumeForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Resume.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form}
    return render(request, 'resume_list.html', context)

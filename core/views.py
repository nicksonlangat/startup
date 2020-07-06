from django.shortcuts import get_object_or_404, render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import *
from .forms import *

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
    
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"
			body = {
 
		    
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
      
	form = ContactForm()
	return render(request, "contact.html", {'form':form})


def apply(request):
  if request.method == 'POST':
    opening_id = request.POST['opening_id']
    opening = request.POST['opening']
    name = request.POST['name']
    email = request.POST['email']
    website = request.POST['website']
    resume = request.POST['resume']
    cover_letter = request.POST['cover_letter']
    user_id = request.POST['user_id']
    recruiter_email = request.POST['recruiter_email']

    #  Check if user has applied already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_applied = Application.objects.all().filter(opening_id=opening_id, user_id=user_id)
      if has_applied:
        messages.error(request, 'You have already submitted an application for this opening')
        return redirect('/')

    application = Application(opening=opening, opening_id=opening_id, name=name, email=email, website=website, cover_letter=cover_letter, user_id=user_id )

    application.save()
    messages.success(request, 'Your request has been submitted successfully!')
    return redirect('/')

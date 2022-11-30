from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings

def home(request):
	return render(request,'portfolioapp/home.html')

def about(request):
	return render(request,'portfolioapp/about.html')

def skills(request):
	return render(request,'portfolioapp/skills.html')

def work(request):
	return render(request,'portfolioapp/work.html')

def education(request):
	return render(request,'portfolioapp/education.html')



def contact(request):
	if request.method == 'POST':
		email = request.POST['email-field']
		name = request.POST['name-field']
		message = request.POST['textarea-field']
		subject = request.POST['subject-field']

		print(name)
		email = EmailMessage(
		subject,
		message,
		settings.EMAIL_HOST_USER,
		[email],
		)
		email.fail_silently=False
		email.send()
		return render(request,'portfolioapp/contact-success.html')

	
	return render(request,'portfolioapp/contact.html')
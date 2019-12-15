from django.shortcuts import render, redirect
from .models import Contact 
from django.http import HttpResponse
# Create your views here.
def contact(request):
	print(request.method)
	if request.method == 'POST':
		name 	= request.POST['name']
		email 	= request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']


		contact = Contact()
		contact.name = name 
		contact.email = email 
		contact.subject = subject
		contact.message = message 
		contact.save()
		return HttpResponse('Your Message has been Sent Succesfully')
		# messages.success(request, 'Your Message has been Sent Succesfully')


	return render(request,'contacts/contact.html')
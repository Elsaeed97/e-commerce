from django.shortcuts import render, redirect
from django.contrib import messages ,auth
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
# Create your views here.


def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		if User.objects.filter(username=username).exists():
			messages.error(request,'This UserName Already Taken')
			return redirect('register')
		else:
			if User.objects.filter(email=email).exists():
				messages.error(request, 'This Email is Already have an account')
				return redirect('register')
			else:
				user = User.objects.create_user(first_name=first_name,username=username,email=email,password=password)
				user.save()
				messages.success(request, 'You Are now Registered and can Log in')
				return redirect('login')
	else:
		return render(request, 'accounts/register.html') 


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			messages.success(request, 'You Are Now Logged in')
			return redirect('dashboard')
		else:
			messages.error(request, 'Invalid UserName or Password')
			return redirect('login')
	else:
		return render(request, 'accounts/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		messages.success(request, 'You Are Logged out')
		return redirect('login') 

def dashboard(request):
	return render(request,'accounts/dashboard.html')

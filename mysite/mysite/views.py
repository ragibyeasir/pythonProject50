from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *


def home(request, ):
	global context
	username = request.user
	customuser = None
	if request.user.is_authenticated:
		customuser = CustomUser.objects.filter(user=username).exists()
		context = {
			'uname': username,
			'customuser': customuser
		}
	return render(request, 'home.html', context)


def another(request):
	return render(request, 'another-page.html')

from django.shortcuts import render
def home(request):
	return render(request, 'home.html')


def another(request):
	return render(request, 'another-page.html')
def messaging(request):
	return render(request, 'messaging.html')

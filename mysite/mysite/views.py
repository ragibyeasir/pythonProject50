from django.shortcuts import render
def home(request):
	return render(request, 'home.html')


def another(request):
	return render(request, 'another-page.html')
def message(request):
	return render(request, 'message.html')
def community(request):
	return render(request, 'community.html')

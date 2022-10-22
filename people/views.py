from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	return render(request, 'people/home.html', context)

def index(request):
	return HttpResponse("Hello, World. This is the people's index")
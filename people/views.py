from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import People, Media, Images
from .forms import MediaForm, ImageForm

# Create your views here.
def home(request):
	context = {}
	return render(request, 'people/home.html', context)

def index(request):
    people_list = People.objects.all()
    #user_list = User.objects.all()
    context = {'people_list':people_list}
    return render(request, 'people/index.html', context)

def get_individual2(request, person_id):
    person = People.objects.get(pk=person_id)
    media_list = Media.objects.all().filter(person=person)
    image_list = Images.objects.all().filter(person=person)
    print(media_list)

    #if this is a POST request we need to process the form data
    if request.method == 'POST':
        #create a form instance and populate it with the data from the request
        mediaform = MediaForm(request.POST, request.FILES)
        #check whether it's valid:
        if mediaform.is_valid():
            #process data in the form.cleaned_data as required
            #...
            #redirect to a new URL:
            mediaform.save()
            print('responseredirect')
            return HttpResponseRedirect(reverse('individual', args=(person.id,)))

    #if a GET (or any other method) we'll create a blank form.
    else:
        mediaform = MediaForm()

    if request.method == 'POST':
        imageform = ImageForm(request.POST, request.FILES)
        if imageform.is_valid():
            #process data in the form.cleaned_data as required
            #...
            #redirect to a new URL:
            imageform.save()
            print('responseredirect')
            return HttpResponseRedirect(reverse('individual', args=(person.id,)))

    #if a GET (or any other method) we'll create a blank form.
    else:
        imageform = ImageForm()

    context = {'person': person,'media_list': media_list, 'image_list':image_list, 'mediaform':mediaform, 'imageform':imageform}
    return render(request, 'people/individual.html', context)

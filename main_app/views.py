from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ExperiencesForm
from .models import City, Experiences, Photo
import uuid
import boto3

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'travelguide1'

class CityCreate(CreateView):
    model = City
    fields = '__all__'
    success_url = '/cities/'


class CityUpdate(UpdateView):
    model = City
    # Disallowing the renaming of a city by excluding the name field
    fields = ['population', 'languages', 'currency']
    success_url = '/cities/'


class CityDelete(DeleteView):
    model = City
    success_url = '/cities/'


# class ExperienceCreate(CreateView):
#   model = Experiences
#   fields = '__all__'
#   form = ExperiencesForm
#   success_url = '/experiences/'

def experiences_create(request):
  if request.method == 'POST':
    form = ExperiencesForm(request.POST)
    form.save()
    return redirect('experiences/')
  form = ExperiencesForm()
  return render(request, 'main_app/experiences_form.html', {'form': form} )


def home(request):
    return HttpResponse('<h1>made a change here Hello here it is /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def cities_index(request):
    cities = City.objects.all()
    return render(request, 'cities/index.html', {'cities': cities})


def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    return render(request, 'cities/citydetail.html', {'city': city})


def experiences_index(request):
    experiences = Experiences.objects.all()
    return render(request, 'experiences/index.html', {'experiences': experiences})


def add_photo(request, city_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, city_id=city_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
          
    return redirect('city_detail', city_id=city_id)


# class City:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, population, languages, currency):
#     self.name = name
#     self.population = population
#     self.languages = languages
#     self.currency = currency

# cities = [
#   City('London', 1400000,'English', 'GBP'),
#   City('New Delhi', 10000000, 'Hindi', 'INR'),
#   City('Paris', 25000000, 'French', 'EUR')
# ]

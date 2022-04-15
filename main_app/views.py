from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ExperiencesForm
from .models import City, Experiences, Photo
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'travelguide1'


class CityCreate(LoginRequiredMixin, CreateView):
    model = City
    fields = '__all__'
    success_url = '/cities/'


class CityUpdate(LoginRequiredMixin, UpdateView):
    model = City
    # Disallowing the renaming of a city by excluding the name field
    fields = ['population', 'languages', 'currency']
    success_url = '/cities/'


class CityDelete(LoginRequiredMixin, DeleteView):
    model = City
    success_url = '/cities/'


class ExperienceUpdate(LoginRequiredMixin, UpdateView):
    model = Experiences
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['eventname', 'eventdate', 'eventtime', 'address', 'eventdescription',
              'eventlink', 'city']
    success_url = '/experiences/'


class ExperienceDelete(LoginRequiredMixin, DeleteView):
    model = Experiences
    success_url = '/experiences/'

# class ExperienceCreate(CreateView):
#   model = Experiences
#   fields = '__all__'
#   form = ExperiencesForm
#   success_url = '/experiences/'


def experiences_create(request):
    if request.method == 'POST':
        form = ExperiencesForm(request.POST)
        form.save()
        return redirect('/experiences/')
    form = ExperiencesForm()
    return render(request, 'main_app/experiences_form.html', {'form': form})


def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)


# def home(request):
#     return HttpResponse('<h1>made a change here Hello here it is /ᐠ｡‸｡ᐟ\ﾉ</h1>')


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


def experience_detail(request, experience_id):
    experience = Experiences.objects.get(id=experience_id)
    return render(request, 'experiences/experiencedetail.html', {'experience': experience})


@login_required
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
        except Exception as e:
            print(e)
            print('x-----error above-----x')

    return redirect('city_detail', city_id=city_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
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

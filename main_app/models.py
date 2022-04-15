from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    languages = models.TextField(max_length=250)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('citydetail', kwargs={'city_id': self.id})


class Experiences(models.Model):
    eventname = models.CharField(max_length=100)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    address = models.TextField(max_length=250)
    eventdescription = models.TextField(max_length=500)
    eventlink = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.eventname

    def get_absolute_url(self):
        return reverse('experiencedetail', kwargs={'experience_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for city_id {self.city_id} @{self.url}"

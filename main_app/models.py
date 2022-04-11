from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    languages = models.TextField(max_length=250)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
         return reverse('citydetail', kwargs={'city_id': self.id})


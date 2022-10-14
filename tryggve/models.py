from pickle import FALSE
from django.db import models
from django.conf import settings

static_url = settings.STATIC_URL
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)
    affliation = models.CharField(max_length=1000)
    team_lead = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class Icon(models.Model):
    name = models.CharField(max_length=100)
    icon = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name

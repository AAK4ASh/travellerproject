from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='images')
    description = models.TextField(default='described')


class People(models.Model):
    personname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='imagesofpeople')
    about = models.TextField(default='about')

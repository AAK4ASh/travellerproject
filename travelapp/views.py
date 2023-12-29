from django.shortcuts import render
from .models import Place
from .models import People
from django.http import HttpResponse


# Create your views here.
def fun(request):
    obje = Place.objects.all()
    personobj = People.objects.all()
    return render(request, 'index.html', {'change': obje, 'person': personobj})

from django.shortcuts import render
from . import models *

# Create your views here.


def index(request):
    return render(request, 'weather_report/index.html')

def crag_forecast(request, selected):
    area = models.Area
    region = models.Region
    crag = models.crag
    location = selected
    return render(request, 'weather_report/crag_forecast.html',
            {
                'area': area, 
                'region': region,
                'crag': crag, 
                'location': location
            })
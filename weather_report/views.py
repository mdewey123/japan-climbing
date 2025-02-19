from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from . import weather_access

def index(request):
    area = Area.objects.all()
    regions = Region.objects.all()
    return render(request, 'weather_report/index.html', {
        "areas": area,
        "regions": regions,
    })

def area_forecast(request, area):
    current_area = get_object_or_404(Area, name=area)
    crags = Crag.objects.all()
    return render(request, 'weather_report/regions.html',
            {
                'area': current_area,
                'crags': crags,
            })

def local_forecast(request, crag):
    crag = get_object_or_404(Crag, slug=crag)
    latitude = crag.latitude
    longitude = crag.longitude
    daily_forecast, hourly_forecast, current_weather = weather_access.get_weather(latitude, longitude)
    return render(request, 'weather_report/crag.html',
            {
                'crag': crag,
                'forecast': current_weather,
                'daily_forecast': daily_forecast,
                "hourly_forecast": hourly_forecast
            })
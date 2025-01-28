from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from . import weather_access

def index(request):
    weather_access
    return render(request, 'weather_report/index.html')

def region_forecast(request, region):
    current_region = get_object_or_404(models.Regions, name=region)
    return render(request, 'weather_report/regions.html',
            {
                'region': region,
            })

def local_forecast(request, crag):
    crag = get_object_or_404(models.Crags, name=crag)
    return render(request, 'weather_report/crag.html',
            {
                'crag': crag,
            })
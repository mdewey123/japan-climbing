from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from . import weather_access

def index(request):
    weather_access
    area = Area.objects.all()
    regions = Region.objects.all()
    return render(request, 'weather_report/index.html', {
        "areas": area,
        "regions": regions,
    })

def area_forecast(request, area):
    current_area = get_object_or_404(Area, name=area)
    return render(request, 'weather_report/regions.html',
            {
                'region': current_area,
            })

def local_forecast(request, crag):
    crag = get_object_or_404(Crags, name=crag)
    return render(request, 'weather_report/crag.html',
            {
                'crag': crag,
            })
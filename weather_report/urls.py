from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crag/forecast/area/<str:area>/", views.area_forecast, name="area_forecast"),
    path("crag/forecast/local/<slug:crag>/", views.local_forecast, name="local_forecast"),
]
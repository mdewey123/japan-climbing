from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("crag/forecast/<str:area>/", views.area_forecast, name="area_forecast"),
    path("crag/forecast/<str:location>/", views.local_forecast, name="local_forecast"),
]
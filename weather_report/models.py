from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class User(AbstractUser):
  watchlist = models.ManyToManyField('Crags')
  home = models.ForeignKey('Regions', on_delete = models.CASCADE)
  nicname = models.CharField(max_length = 69)
  def __str__(self):
    return f"{self.username} ({self.email})"

class Area(models.Model):
  name = models.CharField(max_length=50)
 
  def __str__(self):
    return self.name

class Regions(models.Model):
  area = models.ForeignKey(Area, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)
  elevation = models.DecimalField(max_digits=5, decimal_places=1) 
  
  def __str__(self):
    return self.name

class Crags(models.Model):
  area = models.ForeignKey(Area, on_delete=models.CASCADE)
  region = models.ForeignKey(Regions, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)
  elevation = models.DecimalField(max_digits=5, decimal_places=1)

  def __str__(self):
    return f"{self.name} ({self.latitude}, {self.longitude})"
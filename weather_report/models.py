from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

def User(AbstractUser):
  pass

def Area(models.Model):
  name = models.CharField(max_length=50)
 
  def __str__(self):
    return self.name

def Region(models.Model):
  area = models.foreingkey(Area, on_delete=models.CASCADE)
  name = models.CharField(max_length=50) 
  
  def __str__(self):
    return self.name

def crag(models.Model):
  area = models.foreignkey(Area, on_delete=models.CASCADE)
  region = models.foreingkey(Region, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)

  def __str__(self):
    return f"{self.name} ({self.latitude}, {self.longitude})"

def UserProfile(models.Model):
  user = models.ForeignKey(User, on_delete=CASCADE)

def __str__(self):
  return f"{self.user.username} ({self.user.email})"
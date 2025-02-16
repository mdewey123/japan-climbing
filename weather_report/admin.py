from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Area)
admin.site.register(User)
admin.site.register(Region)
admin.site.register(Crags)
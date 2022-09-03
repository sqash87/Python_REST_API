#Registering the a model in the admin.
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)
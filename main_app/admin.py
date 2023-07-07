from django.contrib import admin
from .models import Cuisine # import the Artist model from models.py
# Register your models here.

admin.site.register(Cuisine) # this line will add the model to the admin panel
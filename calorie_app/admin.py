from django.contrib import admin
from .models import Foodie, Food, Userdetails

# Register your models here.

admin.site.register(Foodie)
admin.site.register(Food)
admin.site.register(Userdetails)
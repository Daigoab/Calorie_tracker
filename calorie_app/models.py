from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Foodie(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    food = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

class Food (models.Model):
    name = models.CharField(max_length=100)
    carbohydrate = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    fats = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    salt = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    sugar = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    total_calory = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    total_calories = models.IntegerField(default=0)

    def total_calories():
        return Food.objects.aggregate(total_calories=models.Sum('calories'))['total_calories']

class Userdetails (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
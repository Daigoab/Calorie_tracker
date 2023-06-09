
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.foodie, name = 'foodies' ),
    path('food/', views.food, name='food'),
    path('userdetails/', views.userdetails, name='userdetails')
]
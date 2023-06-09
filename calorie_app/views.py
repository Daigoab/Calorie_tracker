from django.shortcuts import render, redirect
from .models import Foodie, Food, Userdetails


def foodie(request):
    foodies = Foodie.objects.all().order_by('-id')
    return render(request, 'foodie.html', {'foodies': foodies})

def food(request):
    foods = Food.objects.all().order_by('-id')
    return render(request, 'food.html', {'foods': foods})
    
def userdetails(request):
    userdetails = Userdetails.objects.all().order_by('-id')
    return render(request, 'userdetails.html', {'userdetails': userdetails})
    

def add_food(request):
    # Check if the request is from the admin form
    if '_save' in request.POST:
        # Process the admin form data
        # Assuming the fields in the admin form are 'name' and 'calories'
        name = request.POST['name']
        carbohydrates = request.POST['carbohydrates']
        proteins = request.POST['proteins']
        fats = request.POST['fats']
        salt = request.POST['salt']
        sugar = request.POST['sugar']
        total_calories = request.POST['total_calories']
        food = Food(
            name=name, 
            carbohydrates=carbohydrates, 
            proteins=proteins, 
            fats=fats, salt=salt, 
            sugar=sugar,
            total_calories=total_calories
            )
        food.save()
        return redirect('food') 
    
    return redirect('add_food') 


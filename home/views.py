from django.shortcuts import render, get_object_or_404
from .models import Car


def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)


def inventory(request):
    #this holds all cars in the database 

    inventory_cars = Car.objects.all()

    context = {
        'inventory_cars': inventory_cars
    }
    return render(request, 'home/inventory.html', context)#context contains all data sent
  
  

def about(request):
  

    return render(request, 'home/about.html')

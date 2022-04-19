from django.shortcuts import render, get_object_or_404
from .models import Car
from .filters import CarFilter

def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)


def inventory(request):
    #this holds all cars in the database 

    inventory_cars = Car.objects.all()

    car_list = Car.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    car_list = car_filter.qs

    context = {
        'inventory_cars': inventory_cars,
        'car_list': car_list, 'car_filter': car_filter
    }
    #context contains all data sent
    return render(request, 'home/inventory.html', context)
  
  

def about(request):
  

    return render(request, 'home/about.html')


def car_detail(request, car_id):
    cars = get_object_or_404(Car, id=car_id)

    context = {
        'cars':cars
    }
    return render(request, 'home/detail.html', context)

from django.shortcuts import render
from .models import Car
from .filters import CarFilter

def homepage(request):
    new_cars = Car.objects.all().order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)

def inventory(request):
    car_list = Car.objects.all()
    car_filter = CarFilter(request.GET, queryset=car_list)
    car_list = car_filter.qs

    return render(request, 'home/inventory.html', {'car_list':car_list, 'car_filter': car_filter})
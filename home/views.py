from django.shortcuts import render
from .models import Car



def homepage(request):
    new_cars = Car.objects.order_by('-date_added')[:5]
    data = {'new_cars': new_cars
            }

    return render(request, 'home/index.html', data)

def search_results(request):
    if request.method == "POST":
        searched = request.POST.get('searched', False);
        cars = Car.objects.filter(name__contains=searched)
        return render(request, 'home/search_results.html', {'searched':searched, 'cars':cars})
    else:
        return render(request, 'home/search_results.html', {})
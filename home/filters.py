import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    make = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Car
        fields = ('name', 'color', 'make', 'price')
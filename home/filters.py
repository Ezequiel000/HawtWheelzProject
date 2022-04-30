import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet):
     name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
     price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
     price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
     class Meta:
         model = Car
         fields = ['name', 'color', 'make', 'price', 'type']
from django.urls import path, re_path
from . import views


urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('inventory/', views.inventory, name='inventory'),
   re_path(r'^inventory/$', views.inventory, name='search'),
   ]

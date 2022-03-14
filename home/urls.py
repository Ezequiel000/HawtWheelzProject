from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('search_results', views.search_results, name='search_results' )
   ]

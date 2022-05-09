from django.urls import path
from . import views
from .views import register_request
app_name = 'members'
urlpatterns = [

    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),


]

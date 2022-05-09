from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [

    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('user/', views.user_profile, name='user_profile'),


]

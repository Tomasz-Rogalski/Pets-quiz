
from django.urls import path
from . import views

app_name='quiz'

urlpatterns = [
    path('home', views.home, name='home')
]

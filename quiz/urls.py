
from django.urls import path
from . import views

app_name='quiz'

urlpatterns = [
    path('home', views.home, name='home'),
    path('question/<int:question_id>/', views.question, name='question'),
]

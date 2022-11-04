
from django.urls import path
from . import views

app_name='quiz'

urlpatterns = [
    path('home', views.home, name='home'),
    path('question/<int:game_id>/', views.question, name='question'),
    path('options', views.options, name='options'),
    path('scoreboard/<int:game_id>/', views.scoreboard, name='scoreboard'),
]

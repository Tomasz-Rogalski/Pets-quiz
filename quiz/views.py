from django.shortcuts import render

def home(request):
    context = {}
    return (request, 'quiz/home.html', context)

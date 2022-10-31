from django.shortcuts import render, HttpResponse

def home(request):
    context = {}
    return (request, 'quiz/home.html', context)

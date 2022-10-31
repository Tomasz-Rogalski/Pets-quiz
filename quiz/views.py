from django.shortcuts import render, HttpResponse

def home(request):
    context = {}
    return render(request, 'quiz/home.html', context)

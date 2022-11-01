from django.shortcuts import render
from .models import Question
from random import shuffle

def home(request):
    context = {}
    return render(request, 'quiz/home.html', context)

def question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = [
        question.true_answer,
        question.false_answer1,
        question.false_answer2,
        question.false_answer3,
        ]
    shuffle(answers)

    context = {'question':question, 'answers':answers}
    return render(request, 'quiz/question.html', context)
    

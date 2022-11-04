from django.shortcuts import render, redirect
from .models import Game
from random import shuffle
from .forms import GameForm

def home(request):
    context = {}
    return render(request, 'quiz/home.html', context)

# def question(request, question_id):
#     question = Question.objects.get(id=question_id)
#     answers = [
#         question.true_answer,
#         question.false_answer1,
#         question.false_answer2,
#         question.false_answer3,
#         ]
#     shuffle(answers)

#     context = {'question':question, 'answers':answers}
#     return render(request, 'quiz/question.html', context)

def question(request, game_id):

    game = Game.objects.get(id=game_id)
    player_answer = request.POST.get('player_answer')

    while not game.is_finished:
        if request.method == 'POST':
            prev_question = game.get_question()
            if prev_question.answer_is_true(player_answer):
                game.add_score()
            
            game.current_question_index+=1            
            game.save()
            if game.current_question_index >= len(game):
                game.is_finished = True
                game.save()
                continue
            question = game.get_question()
            answers = question.get_shuffled_answers()

        elif request.method != 'POST':
            game.start_new_game()
            question = game.get_question()
            answers = question.get_shuffled_answers()

        context = {'question':question, 'answers':answers, 'game':game}
        return render(request, 'quiz/question.html', context)
    
    else:
        return redirect('quiz:home')

def options(request):
    if request.method != 'POST':
        form = GameForm()
        context = {'form':form}
        return render (request, 'quiz/options.html', context)
    else:
        form = GameForm(data=request.POST)
        if form.is_valid:
            game=form.save()
        return redirect ('quiz:question', game.id)


    

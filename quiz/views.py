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

    
    
    print ('******************************')
    print ('ID', game.id)
    print (request.POST)
    print ('questionset', game.questionset)
    print ('currentq', game.current_question_nr)
    print ('******************************')    

    if game.current_question_nr >= game.total_questions_nr:
        return redirect('quiz:home') #summary
    else:
        if request.method == 'POST':
            # if game.question.answer_is_true(player_answer):
            #     game.add_score()
            game.get_new_question()
            game.save()
            question = game.question
            question.shuffle_answers()
            answers = question.answers

        elif request.method != 'POST':
            game.start_new_game()
            print ('questionset2', game.questionset)
            question = game.question
            question.shuffle_answers()
            print ('questionset3', game.questionset)
            answers = question.answers
            game.save()
            
    context = {'question':question, 'answers':answers, 'game_id':game.id}
    return render(request, 'quiz/question.html', context)

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


    

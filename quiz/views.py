from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm

def home(request):
    '''Render home page'''
    context = {}
    return render(request, 'quiz/home.html', context)

def question(request, game_id):
    '''Render single question page'''
    game = Game.objects.get(id=game_id)
    player_answer = request.POST.get('player_answer')
    pet = game.pet

    while not game.is_finished:
        if request.method == 'POST':
            # questions [2:]
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
            answers = [('A', answers[0]),
                    ('B', answers[1]),
                    ('C', answers[2]),
                    ('D', answers[3]),
            ]
            # pet reaction
            key = pet.roll_reaction_key()
            pet_answer = pet.roll_answer(question)
            false_answer = question.get_random_false_answer()
            pet_reaction = pet.check_reaction_key(key=key, pet_answer=pet_answer, false_answer=false_answer)

        elif request.method != 'POST':
            # first question
            if not game.questionset.all():
                # If questionset is empty roll questions
                game.start_new_game()
            question = game.get_question()
            answers = question.get_shuffled_answers()
            answers = [('A', answers[0]),
                    ('B', answers[1]),
                    ('C', answers[2]),
                    ('D', answers[3]),
            ]
            #first pet reaction
            pet_reaction = "I will try to help you but remember, it's your test."

        context ={'question':question, 'answers':answers, 'game':game, 'pet_reaction': pet_reaction}
        return render(request, 'quiz/question.html', context)
    else:
        return redirect('quiz:scoreboard', game.id)

def options(request):
    '''Render pre-game page with basic game options form'''
    if request.method != 'POST':
        form = GameForm()
        context = {'form':form}
        return render (request, 'quiz/options.html', context)
    else:
        form = GameForm(data=request.POST)
        if form.is_valid:
            game=form.save()
        return redirect ('quiz:question', game.id)


def scoreboard(request, game_id=0):
    '''Render scoreboard page'''

    context= {}
    if game_id:
        player_game = Game.objects.get(id=game_id)
        context['game']=player_game

    games = list(Game.objects.filter(is_finished=True).order_by('-total_score'))
    scoreboard_rows = 10

    while len(games) < scoreboard_rows:
        games.append(None)

    games = enumerate((games)[:scoreboard_rows])
    context['games']=games

    return render(request, 'quiz/scoreboard.html', context)

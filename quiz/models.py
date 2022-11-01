from django.db import models
from random import shuffle

class Category(models.Model):
    """Category type of questions, first of 2 base game options"""
    name = models.CharField(max_length = 24)

    def __str__(self):
        return self.name

class Pet(models.Model):
    """Player's companion, second of base game options"""
    name = models.CharField(max_length = 24)

    def __str__(self):
        return self.name

class Question(models.Model):
    '''Single question model'''

    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    text = models.TextField()

    true_answer = models.CharField(max_length=64)
    false_answer1 = models.CharField(max_length=64)
    false_answer2 = models.CharField(max_length=64)
    false_answer3 = models.CharField(max_length=64)

class Game(models.Model):
    'Model with game statistics and options'
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    pet = models.ForeignKey(Pet, on_delete= models.PROTECT)

    questionset = []

    game_score = 0
    current_question_nr = 0
    game_questions_nr = 3
    is_finished =models.BooleanField(defalt=False)


    def __init__(self):
        "Create and shuffle questionset"
        self.questionset = list(Question.objects.filter(category=self.category))
        shuffle(self.questionset)
        self.questionset = self.questionset[:3]

    def get_new_question(self):
        self.current_question_nr += 1
        for question in self.questionset:            
            yield question

    




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

    answers = [true_answer,false_answer1,false_answer2,false_answer3,]

    def shuffle_answers(self):
        shuffle(self.answers)

    def answer_is_true(self, answer):
        if answer == self.true_answer:
            return True
        else:
            return False


class Game(models.Model):
    'Model with game statistics and options'
    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    pet = models.ForeignKey(Pet, on_delete= models.PROTECT)
    player_name = models.CharField(max_length = 24)
    is_finished =models.BooleanField(default=False)

    total_score = 0
    current_question_nr = 0
    total_questions_nr = 3

    questionset = []
    question = None

    def get_category_questions(self):
        self.questionset = Question.objects.filter(category=self.category)

    def shuffle_questions(self):
        shuffle(list(self.questionset))

    def create_questionset(self):
        self.questionset = self.questionset[:self.total_questions_nr]

    def get_new_question(self):        
        self.question= self.questionset[self.current_question_nr]
        self.total_questions_nr += 1

    def start_new_game(self):
        "Create, shuffle questionset and get first question"
        self.get_category_questions()
        self.shuffle_questions()
        self.create_questionset()
        self.get_new_question()    

    def add_score(self):        
        self.total_score += 10

    




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

    def get_shuffled_answers(self):
        answers = [self.true_answer,
            self.false_answer1,
            self.false_answer2,
            self.false_answer3,]
        shuffle(answers)
        return answers

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

    total_score = models.IntegerField(default = 0)
    current_question_index = models.IntegerField(default = 0)
    total_number_of_questions = models.IntegerField(default = 5)

    questionset = models.ManyToManyField(Question)

    def __len__(self):
        return self.total_number_of_questions

    def get_question(self):        
        return list(self.questionset.all())[self.current_question_index]

    def start_new_game(self):
        "Create, shuffle questionset and get first question"
        questions = list(Question.objects.filter(category=self.category))
        shuffle(questions)
        questions = questions[:self.total_number_of_questions]

        for question in questions:
            self.questionset.add(question)
        self.save()

    def add_score(self):        
        self.total_score += 10


    




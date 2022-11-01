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
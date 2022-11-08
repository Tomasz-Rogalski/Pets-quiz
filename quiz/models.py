from django.db import models
from random import shuffle, randint, choice

class Category(models.Model):
    """Category type of questions, first of 2 base game options"""
    name = models.CharField(max_length = 24)

    def __str__(self):
        return self.name

class Pet(models.Model):
    """Player's companion, second of base game options"""
    name = models.CharField(max_length = 24)

    proudness = models.IntegerField(default=5) 
    helpfulness = models.IntegerField(default=5)
    confidnece = models.IntegerField(default=5)    

    knowledge = models.IntegerField(default=5)      

    def __str__(self):
        return self.name


    def roll_reaction_success(self, trait):
        '''If pet's trait is high, retrun succes (1)'''
        if randint(0, 10) < trait:
            return 1
        else: 
            return 0
    
    def roll_reaction_key(self):
        '''roll dictionary key for pet reaction'''
        traits = [self.helpfulness, self.confidence, self.proudness]
        key = ''
        for trait in traits:
            result = self.roll_reaction_success(trait)
            key += str(result)
        return key

    def check_reaction_key(self, key, answer):
        '''Pet reaction'''
        reactions = {
            '100':"You must be kidding, you should know it.",
            '110':f"Poor human, the answer is {answer}.",
            '111':f"So easy. It's {answer}.",
            '010':f"I have no idea what is it, maybe {answer}?",
            '011':f"I know it, the answer is {answer}.",
            '000':'I have no idea what is it.',
            '001':f"I'm sure it is not {answer}.",            
        }
        return reactions[key]

    def roll_answer(self, question):
        '''Return true answer if pet knows it or false '''
        if self.roll_reaction_success(self.knowledge):
            return question.true_answer
        else:
            return question.get_random_false_answer()


class Question(models.Model):
    '''Single question model'''

    category = models.ForeignKey(Category, on_delete= models.PROTECT)
    text = models.TextField()

    true_answer = models.CharField(max_length=64)
    false_answer1 = models.CharField(max_length=64)
    false_answer2 = models.CharField(max_length=64)
    false_answer3 = models.CharField(max_length=64)

    def get_random_false_answer(self):
        false_answers = [self.false_answer1, self.false_answer2, self.false_answer3]
        return choice(false_answers)

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


    




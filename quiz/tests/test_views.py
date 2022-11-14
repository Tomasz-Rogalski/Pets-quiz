from django.test import Client, TestCase
from django.urls import reverse
from quiz.models import Question, Game, Pet, Category

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        
        self.category = Category.objects.create(name='testcategory')
        self.pet = Pet.objects.create(name='testpet',
                                            proudness = 5,
                                            helpfulness = 5,
                                            confidnece = 5,
                                            knowledge = 5,)
        
        self.question = Question.objects.create(
            category = self.category,
            text = 'test question text',
            true_answer = 'true',
            false_answer1 = 'false',
            false_answer2 = 'false',
            false_answer3 = 'false',
        )

        self.game = Game.objects.create(
            category = self.category,
            pet = self.pet,
            player_name = 'test_player',
            total_number_of_questions = 1,
            is_finished = False
        )
        for num in range(10):
            self.game.questionset.add(self.question)

        self.home_url = reverse('quiz:home')
        self.options_url = reverse('quiz:options')
        self.question_url = reverse('quiz:question', args=[1])
        self.scoreboard_url = reverse('quiz:scoreboard', args=[1])
        
    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/home.html')

    def test_options_GET(self):
        response = self.client.get(self.options_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/options.html')
    
    def test_options_POST(self):
        
        response = self.client.post(self.options_url, 
                                {'player_name': 'test_player', 'category': '1', 'pet': '1'},
                                )

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Game.objects.first().player_name, 'test_player')
    
    def test_scoreboard_POST(self):
        response = self.client.get(self.scoreboard_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/scoreboard.html')
    

    def test_question_GET(self):
        response = self.client.get(self.question_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'quiz/question.html')

    def test_quiestion__POST_is_finished(self):

        self.game.is_finished = True

        response = self.client.post(self.question_url, {'player_answer': 'sth'})

        self.assertEquals(response.status_code, 302)
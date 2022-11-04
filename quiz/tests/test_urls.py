from django.urls import resolve, reverse

class TestUrls():
    
    def test_home_url(self):
        path = reverse('quiz:home')
        assert resolve(path).view_name == 'quiz:home'

    def test_options_url(self):
        path = reverse('quiz:options')
        assert resolve(path).view_name == 'quiz:options'

    def test_question_url(self):
        path = reverse('quiz:question', kwargs = {'game_id': 1})
        assert resolve(path).view_name == 'quiz:question'

    def test_scoreboard_url(self):
        path = reverse('quiz:scoreboard', kwargs = {'game_id': 1})
        assert resolve(path).view_name == 'quiz:scoreboard'
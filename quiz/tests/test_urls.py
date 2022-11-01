from django.urls import resolve, reverse

class TestUrls():
    
    def test_home_url(self):
        path = reverse('quiz:home')
        assert resolve(path).view_name == 'quiz:home'

    def test_question_url(self):
        path = reverse('quiz:question', kwargs = {'question_id': 1})
        assert resolve(path).view_name == 'quiz:question'
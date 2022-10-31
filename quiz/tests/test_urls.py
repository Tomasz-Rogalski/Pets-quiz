from django.urls import resolve, reverse

class TestUrls():
    
    def test_home_url(self):
        path = reverse('quiz:home')
        assert resolve(path).view_name == 'quiz:home'
from quiz.models import Category, Question
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels():   
    
    def test_category_str(self):
        category = Category.objects.create(name='MyTestCategory')
        assert str(category) == category.name

    # def test_category_str(self):
    #     category = mixer.blend('quiz.Category', name='MyTestCategory')
    #     assert str(category) == category.name

    def test_pet_str(self):
        pet = Category.objects.create(name='MyTestPet')
        assert str(pet) == pet.name
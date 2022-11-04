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

    def test_question_get_shuffled_answers(self):
        question = mixer.blend('quiz.Question', 
                                true_answer = 't1',
                                false_answer1 = 'f1',
                                false_answer2 = 'f2',
                                false_answer3 = 'f3',)
        answers = question.get_shuffled_answers()
        assert len(answers) == 4 and 'f3' in answers

    def test_question_answer_is_true(self):
        question = mixer.blend('quiz.Question', true_answer = 't1',)
        assert question.answer_is_true('t1') == True

    def test_game_len_default(self):
        game = mixer.blend('quiz.Game')
        assert len(game) == 5

    def test_game_len_custom(self):
        game = mixer.blend('quiz.Game', total_number_of_questions=10)
        assert len(game) == 10

    def test_game_add_score(self):
        game = mixer.blend('quiz.Game')
        game.add_score()
        assert game.total_score == 10

    def test_game_add_score(self):
        game = mixer.blend('quiz.Game')
        new_question = mixer.blend('quiz.Question')
        game.questionset.add(new_question)

        question = game.get_question()

        assert question == new_question

        


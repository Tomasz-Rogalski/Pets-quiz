from quiz.models import Category
from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels():   
    
    def test_category_str(self):
        category = Category.objects.create(name='MyTestCategory')
        assert str(category) == category.name

    def test_pet_str(self):
        pet = Category.objects.create(name='MyTestPet')
        assert str(pet) == pet.name

    def test_pet_roll_reaction_succes(self):
        pet = mixer.blend('quiz.Pet', knowledge = 5)
        result = pet.roll_reaction_success(pet.knowledge)
        assert result == 1 or result == 0

    def test_pet_roll_reaction_key(self):
        pet = mixer.blend('quiz.Pet', helpfulness=5, proudness=5, confidence=5)
        result = pet.roll_reaction_key()
        assert len(result)==3

    def test_pet_roll_answer(self):
        pet = mixer.blend('quiz.Pet', knowledge=11)
        question = mixer.blend('quiz.Question', 
                                true_answer = 't1',
                                false_answer1 = 'f1',
                                false_answer2 = 'f2',
                                false_answer3 = 'f3',)

        assert pet.roll_answer(question) == question.true_answer

    def test_pet_check_reaction_key(self):
        pet = mixer.blend('quiz.Pet',)
        key = '111'
        pet_answer = 'example_answer'
        false_answer ='false'
        assert pet.check_reaction_key(key, pet_answer, false_answer) == "So easy. It's example_answer."

    def test_question_get_shuffled_answers(self):
        question = mixer.blend('quiz.Question', 
                                true_answer = 't1',
                                false_answer1 = 'f1',
                                false_answer2 = 'f2',
                                false_answer3 = 'f3',)
        answers = question.get_shuffled_answers()
        assert len(answers) == 4 and 'f3' in answers

    def test_question_get_random_false_answer(self):
        question = mixer.blend('quiz.Question', 
                                true_answer = 't1',
                                false_answer1 = 'f1',
                                false_answer2 = 'f2',
                                false_answer3 = 'f3',)
        false_answers = [
                        question.false_answer1,
                        question.false_answer2,
                        question.false_answer3,
                        ]
        assert question.get_random_false_answer() in false_answers


    def test_question_answer_is_true(self):
        question = mixer.blend('quiz.Question', true_answer = 't1',)
        assert question.answer_is_true('t1') == True

    def test_game_len_default(self):
        game = mixer.blend('quiz.Game')
        assert len(game) == 10

    def test_game_len_custom(self):
        game = mixer.blend('quiz.Game', total_number_of_questions=5)
        assert len(game) == 5

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

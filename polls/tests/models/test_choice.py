from django.test import TestCase
import sure

class TestChoice(TestCase):
    def test_choice_model_exists(self):
        from polls.models import Choice

    def test_create_choice(self):
        from polls.models import Question, Choice
        question = Question.objects.create(text="Test create choice")
        choice = Choice.objects.create(question=question, text="test choice text")

        choice2 = Choice(text="test choice 2")
        question.choices.add(choice2)
        question.save()

        question.choices.count().should.equal(2)
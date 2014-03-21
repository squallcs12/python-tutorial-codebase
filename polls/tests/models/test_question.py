from django.test import TestCase
import sure

class TestQuestion(TestCase):
    def test_question_model_exists(self):
        from polls.models import Question

    def test_create_question(self):
        from polls.models import Question
        question = Question.objects.create(text="Test poll question")
        question.should_not.be.none

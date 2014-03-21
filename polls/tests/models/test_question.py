from django.test import TestCase

class TestQuestion(TestCase):
    def test_question_model_exists(self):
        from polls.models import Question

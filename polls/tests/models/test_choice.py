from django.test import TestCase

class TestChoice(TestCase):
    def test_choice_model_exists(self):
        from polls.models import Choice

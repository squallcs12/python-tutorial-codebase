from django.test.testcases import TestCase
from django.test.client import Client
from polls.tests.factories import QuestionFactory
import sure

class TestPollsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.questions = []
        for i in range(0, 10):
            self.questions.append(QuestionFactory.create())

    def test_index_page(self):
        response = self.client.get('/')
        response.status_code.should.equal(200)
        for question in self.questions:
            response.content.should.contain(question.text)
from django.test.testcases import TestCase
from django.test.client import Client
from polls.tests.factories import QuestionFactory, ChoiceFactory
import sure

class TestPollsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.questions = []
        for i in range(0, 10):
            question = QuestionFactory.create()
            question.save()
            self.questions.append(question)

        for i in range(0, 4):
            choice = ChoiceFactory()
            choice.question = self.questions[0]
            choice.save()

    def test_index_page(self):
        response = self.client.get('/')

        response.status_code.should.equal(200)
        response.content.should.contain("Polls Index")
        for question in self.questions:
            response.content.should.contain(question.text)

    def test_poll_details_page(self):
        question = self.questions[0]
        response = self.client.get(question.get_absolute_url())

        response.status_code.should.equal(200)
        response.content.should.contain("Polls Details")
        response.content.should.contain(question.text)

        for choice in question.choices.all():
            response.content.should.contain(choice.text)

    def test_vote_poll(self):
        question = self.questions[0]
        response = self.client.post(question.get_absolute_url(), {
            'choice_id': question.choices.all()[0].id
            })
        response.status_code.should.equal(302)
        response.has_header("location").should.be.true
        response['location'].should.contain(question.get_absolute_url())

        question.choices.all()[0].votes.should.equal(1)

    def test_vote_wrong_choice(self):
        question = self.questions[0]
        response = self.client.post(question.get_absolute_url(), {
            'choice_id': 0
            })
        response.status_code.should.equal(404)
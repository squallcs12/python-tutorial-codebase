# -*- coding: utf-8 -*-
from lettuce import step
from polls.features.steps.lettuce_support import browser, visit_url
from polls.tests.factories import QuestionFactory, ChoiceFactory

@step(u'some questions are in the database')
def some_questions_are_in_the_database(step):
    for i in range(0, 5):
        question = QuestionFactory.create()
        question.save()

@step(u'I visit the home page')
def i_visit_the_home_page(step):
    visit_url("/")

@step(u'I should see a list of polls questions')
def i_should_see_a_list_of_polls_questions(step):
    questions = browser().find_elements_by_css_selector(".questions .question")
    assert len(questions) > 0
from django.template.response import TemplateResponse
from django.views.generic.base import View
from django.shortcuts import get_object_or_404, redirect

from polls.models import Question, Choice

class QuestionView(View):

    template = "polls/question.html"

    def get(self, request, question_id=None):
        context = {}
        context['question'] = get_object_or_404(Question, pk=question_id)
        return TemplateResponse(request, self.template, context)

    def post(self, request, question_id=None):
        choice_id = request.POST.get("choice_id", None)

        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes += 1
        choice.save()

        return redirect("poll_detail", question_id=question_id)
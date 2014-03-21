from django.conf.urls import patterns, include, url

from polls.views import IndexView, QuestionView

urlpatterns = patterns('',
    url(r'^detail/(?P<question_id>\d+)$', QuestionView.as_view(), name="poll_detail"),
    url(r'^$', IndexView.as_view(), name='home'),
)

from django.db import models

class Choice(models.Model):
    text = models.TextField()
    question = models.ForeignKey("polls.Question", related_name="choices")
    votes = models.IntegerField(default=0)

    class Meta:
        app_label = "polls"
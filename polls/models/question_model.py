from django.db import models

class Question(models.Model):
    text = models.TextField()

    class Meta:
        app_label = "polls"
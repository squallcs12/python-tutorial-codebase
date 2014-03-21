from django.db import models
from django.core.urlresolvers import reverse

class Question(models.Model):
    text = models.TextField()

    class Meta:
        app_label = "polls"

    def get_absolute_url(self):
        return reverse("poll_detail", kwargs={"question_id": self.id})
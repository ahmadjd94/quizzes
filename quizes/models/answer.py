from django.db import models
from .question import Question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField()

    objects = models.Manager()

    class Meta:
        unique_together = (("question", "choice_text"),)

    def __str__(self):
        return self.choice_text

from django.db import models
from .question import Question

from django.core.exceptions import ValidationError


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    choice_text = models.CharField(max_length=200)
    correct = models.BooleanField()

    objects = models.Manager()

    class Meta:
        unique_together = (("question", "choice_text"),)

    def __str__(self):
        return self.choice_text

    def validate_unique(self,*args,**kwargs):
        if self.correct:
            for choice in self.question.answers.all().values("correct"):
                if choice["correct"]:
                    raise ValidationError("the question referenced already contains a correct answer")

        return super(Choice, self).validate_unique(*args, **kwargs)

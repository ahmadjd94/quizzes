from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=1024)

    objects = models.Manager()

    class Meta:
        verbose_name = "quiz"
        verbose_name_plural = "quizzes"

    def __str__(self):
        return self.name




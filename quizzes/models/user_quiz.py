from django.db import models
from django.contrib.auth.models import User
from .quiz import Quiz


class UserQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="users")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    mark = models.IntegerField()


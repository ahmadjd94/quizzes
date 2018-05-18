from django.db import models
from .quiz import Quiz


class Question(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name="questions")
	name = models.CharField(max_length=20)
	text = models.CharField(max_length=200)

	def __str__(self):
		return self.name

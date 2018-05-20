from django.db import models
from django.contrib.auth.models import User
from .quiz import Quiz


class Mark(models.Model):
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="marks")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="marks")
	result = models.IntegerField(max_length=20)

	objects = models.Manager()

	class Meta:
		verbose_name = "Mark"
		verbose_name_plural = "Marks"


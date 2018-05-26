from django.db import models
from django.contrib.auth.models import User

from .video import Video


class Comment(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
	title = models.CharField(max_length=50)
	body = models.CharField(max_length=500)

	objects = models.Manager()

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"

	def __str__(self):
		return self.title

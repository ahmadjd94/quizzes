from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="feedback")
    title = models.CharField(max_length=15)
    body = models.CharField(max_length=15)

    objects = models.Manager()

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"

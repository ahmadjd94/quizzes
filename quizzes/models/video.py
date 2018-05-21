from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=48)
    widget = models.CharField(max_length=2048)
    story = models.CharField(max_length=2048)

    objects = models.Manager()

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.name

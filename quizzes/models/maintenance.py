from django.db import models
from .service import Service


class Maintenance(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="maintenance")
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

    objects = models.Manager()

    class Meta:
        verbose_name = "maintenance"
        verbose_name_plural = "maintenance"

    def __str__(self):
        return self.name

from django.db import models


class Service(models.Model):
	name = models.CharField(max_length=200)

	objects = models.Manager()

	class Meta:
		verbose_name = "service"
		verbose_name_plural = "services"

	def __str__(self):
		return self.name
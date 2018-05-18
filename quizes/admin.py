from django.contrib import admin
from .models import Choice, Quiz, Question

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)

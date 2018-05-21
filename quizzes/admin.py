from django.contrib import admin
from .models import Choice, Quiz, Question, Video

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Video)

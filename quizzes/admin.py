from django.contrib import admin
from .models import(Choice, Quiz, Question,
                    Video, Comment, Service, Maintenance, Feedback)

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Service)
admin.site.register(Maintenance)
admin.site.register(Feedback)

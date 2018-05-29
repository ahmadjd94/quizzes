"""quizzes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import quizzes, quiz, register, home, marks, videos, video, video_comment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', register, name="register"),
    path('quizzes', quizzes),
    path('videos', videos),
    path('videos/<int:id>', video),
    path('videos/<int:video_id>/comments', video_comment),
    path('quizzes/marks', marks),
    path('quizzes/<int:id>', quiz),
    path('', home, name="home"),
    path('oauth/', include('social_django.urls', namespace='social')),  # <--
]

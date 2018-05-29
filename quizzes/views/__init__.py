from .quiz import quiz, quizzes
from .user_views import register
from .main import home
from .marks import marks
from .videos import videos, video, video_comment
from .service import service, services
from .feedback import feedback
from .terms import terms

__all__ = ("quiz", "quizzes", "register", 'marks', 'videos',
           'video', 'video_comment', "service", "services",
           "feedback", "terms")


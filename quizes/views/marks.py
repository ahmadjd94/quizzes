from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.forms import Form

from ..models import Mark


def marks(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    kwargs = {"user":request.user.id}
    marks_data = Mark.objects.filter(**kwargs)
    for i in marks_data:
        print(i.result)
        print(i.quiz)

    return render(
        request, 'quizzes/marks.html',
        {
            "marks":
                marks_data,
        }
    )


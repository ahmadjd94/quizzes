from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.forms import Form

from ..models import Quiz, Choice, Mark


def quizzes(request):

    quizzes_data = Quiz.objects.all()
    logged_in = False
    if request.user.is_authenticated:
        logged_in = True
    return render(
        request, 'quizzes/index.html',
        {
            "quizzes":
                quizzes_data,
            "logged_id": logged_in
        }
    )


def quiz(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    print(kwargs)
    quiz_object = Quiz.objects.get(**kwargs)
    quiz_id = kwargs["id"]
    if request.method == 'POST':

        f = Form(request.POST)

        ids = []
        for k, v in f.data.items():
            if k == "csrfmiddlewaretoken":
                continue
            else:
                ids += v
        kwargs = {"id__in": ids}
        choices = Choice.objects.filter(**kwargs).values("correct")

        correct_choices = 0
        for choice in choices:
            if choice["correct"]:
                correct_choices += 1

        mark_kwargs = {"user": request.user.id, "quiz": quiz_id }
        exam_result = int(correct_choices / len(ids) * 100)
        try:
            mark = Mark.objects.get(**mark_kwargs)
            mark .result = exam_result
        except Exception:
            mark = Mark(user=request.user, quiz=quiz_object, result = exam_result)

        mark.save()

        result = {
            "correct_choices": correct_choices,
            "total_questions": len(ids),
            "mark": correct_choices / len(ids) * 100
        }

        return render(
            request, 'quizzes/result.html',
            result
        )

    return render(
        request, 'quizzes/take.html',
        {
            'quiz': quiz_object,
            "questions": [
                {
                    "name": question.name,
                    "body": question.body,
                    "answers": question.answers.all()
                } for question in quiz_object.questions.all()
            ]
        }
    )

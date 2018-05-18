from django.http import HttpResponse
from django.shortcuts import render
from django.forms import Form

from ..models import Quiz, Choice


def quizzes(request):

    quizzes_data = Quiz.objects.all()
    return render(
        request, 'quizzes/index.html',
        {
            "quizzes":
                quizzes_data
        }
    )


def quiz(request, *args, **kwargs):
    quiz_object = Quiz.objects.get(**kwargs)

    if request.method == 'POST':
        questions_count = quiz_object.questions.all().count()

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
        result = {
            "correct_choices": correct_choices,
            "total_questions": len(ids),
            "mark": correct_choices/len(ids) * 100
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
                    "answers": question.answers.all()
                } for question in quiz_object.questions.all()
            ]
        }
    )

from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render

from ..models import Feedback
from ..forms import FeedbackForm


def feedback(request, *args, **kwargs):
    if not request.user.is_authenticated:

        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    if request.method == "GET":

        return render(
            request, 'feedback/form.html', {
                "form": FeedbackForm
            }
        )
    elif request.method == "POST":

        title = request.POST.get("title")
        body = request.POST.get("body")

        feedback = Feedback(user=request.user, title=title, body=body)
        feedback.save()

        return render(
            request, 'feedback/success.html', {}
        )
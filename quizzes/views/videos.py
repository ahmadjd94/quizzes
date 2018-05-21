from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render

from ..models import Video, Comment
from ..forms import CommentForm


def videos(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    videos_data = Video.objects.all()

    return render(
        request, 'videos/index.html',
        {
            "videos":
                videos_data,
        }
    )


def video(request, *args, **kwargs):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    video_data = Video.objects.get(**kwargs)
    comments = [comment for comment in video_data.comments.prefetch_related()]

    return render(
        request, 'videos/video.html',
        {
            "video":
                video_data,
            "comments":
                comments,
            "form":
                CommentForm()
        }
    )

def video_comment(request, *args, **kwargs):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.POST:
        video_kwargs = {"id": kwargs["video_id"]}
        video_data = Video.objects.get(**video_kwargs)
        print(request.body)
        title = request.POST.get("title")
        body = request.POST.get("body")
        comment = Comment(user=request.user,video=video_data, title=title, body=body)
        comment.save()
        # comments = video_data.comments.all()
        form = CommentForm

        return render(
            request, 'comments/success.html',
            {
                "video":
                    video_data,
                # "comments":
                #     comments,
                "form":
                    CommentForm
            }
        )



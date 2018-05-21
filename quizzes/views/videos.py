from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render

from ..models import Video


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

    return render(
        request, 'videos/video.html',
        {
            "video":
                video_data,
        }
    )


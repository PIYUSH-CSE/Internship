from django.shortcuts import render

from .models import *


def files(request):
    if request.method == 'POST':
        video_file = request.FILES.get('video_file')
        text_file = request.FILES.get('text_file')
        if video_file and text_file:
            file = File(video_file=video_file, text_file=text_file)
            file.save()
            return render(request, 'intern/upload_file.html')
    return render(request, 'intern/upload_file.html')





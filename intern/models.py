from django.db import models

# Create your models here.


class File(models.Model):
    video_file = models.FileField(upload_to='video_file/')
    text_file = models.FileField(upload_to='text_file/')
    timestamp = models.DateTimeField(auto_now_add=True)


from django.urls import path
from .views import *

urlpatterns = [
    path('', files, name='upload_file'),
    ]
from django.urls import path

from main.views import ImageFaceDetect, LiveVideoFaceDetect

app_name = 'face-detect'

urlpatterns = [
    path('face-detect/image/', ImageFaceDetect.as_view(), name='image'),
    path('face-detect/video/', LiveVideoFaceDetect.as_view(), name='live_video'),
]

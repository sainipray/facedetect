from django.urls import path

from .views import ImageFaceDetect, LiveVideoFaceDetect

urlpatterns = [
    path('image', ImageFaceDetect.as_view(), name='image'),
    path('video', LiveVideoFaceDetect.as_view(), name='live_video'),
]


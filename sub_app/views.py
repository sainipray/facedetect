from __future__ import unicode_literals
 
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.generic import TemplateView

from .py_files.detect import get_face_detect_data


def upload_file(image):
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    uploaded_file_url = fs.path(filename)
    return uploaded_file_url


class ImageFaceDetect(TemplateView):
    template_name = 'image.html'

    def post(self, request, *args, **kwargs):
        data = request.POST.get('image')
        try:
            image_data = get_face_detect_data(data)
            if image_data:
                return JsonResponse(status=200, data={'image': image_data, 'message': 'Face detected'})
        except Exception as e:
            pass
        return JsonResponse(status=400, data={'errors': {'error_message': 'No face detected'}})


class LiveVideoFaceDetect(TemplateView):
    template_name = 'video.html'

    def post(self, request, *args, **kwargs):
        return JsonResponse(status=200, data={'message': 'Face detected'})


from django.urls import path, include
from .views import *
from .api import PDFUploadApi
from rest_framework import routers


urlpatterns = [
    path('', pdf_upload_view, name='pdf_upload'),
    path('tagcloud/', PDFUploadApi.as_view(), name='pdf_upload_api'),
]

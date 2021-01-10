from rest_framework.test import APITestCase
from rest_framework import status
from os import listdir
from os.path import isfile, join
from django.conf import settings
from constants import PDF_FILES_DIR, IMAGE_FILES_DIR
import requests

# Create your tests here.


class PDFUploadApiTestCase(APITestCase):

    def test_pdf_file(self):
        test_files_dir = '{}{}'.format(settings.BASE_DIR, PDF_FILES_DIR)
        files = [join(test_files_dir, f) for f in listdir(test_files_dir)
                 if isfile(join(test_files_dir, f))]
        with open(files[0], 'rb') as fp:
            data = {"file": ('sample.pdf', fp, 'application/pdf')}
            response = requests.post("http://127.0.0.1:8000/tagcloud/",
                                     files=data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_image_file(self):
        test_files_dir = '{}{}'.format(settings.BASE_DIR, IMAGE_FILES_DIR)
        files = [join(test_files_dir, f) for f in listdir(test_files_dir)
                 if isfile(join(test_files_dir, f))]
        with open(files[0], 'rb') as fp:
            data = {"file": ('sample.jpg', fp, 'image/jpg')}
            response = requests.post("http://127.0.0.1:8000/tagcloud/",
                                     files=data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_file(self):
        response = requests.post("http://127.0.0.1:8000/tagcloud/",
                                 files=None)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

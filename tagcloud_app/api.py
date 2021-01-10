from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PDFUploadSerializer


class PDFUploadApi(APIView):
    """
    PDF data upload API
    :param request: tag cloud file
    :return:
    """

    def post(self, request, *args, **kwargs):
        fileobj = request.FILES.get('file')
        serializer = PDFUploadSerializer(data=request.FILES)
        if serializer.is_valid(raise_exception=True):
            img_str = serializer.create()

        return Response(img_str, status=status.HTTP_200_OK)

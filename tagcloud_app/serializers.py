from rest_framework import serializers

from utils import *


def file_validator(file):
    if file.content_type != "application/pdf":
        raise serializers.ValidationError("File type is not correct.")
    return file


class PDFUploadSerializer(serializers.Serializer):
    file = serializers.FileField(validators=[file_validator])

    def create(self):
        fileobj = self.validated_data.get('file')

        images = pdf_to_image(fileobj)  # converting pdf to images

        text = ocr(images)  # Performing OCR on images and fetching the text

        wordcloud = create_word_cloud(text)  # Creating Word cloud

        # Converting word_Cloud object to image string to pass in response
        buffer = io.BytesIO()
        wordcloud.save(buffer, "PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return img_str

from pdf2image import convert_from_bytes
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from django.conf import settings
from constants import POPPLER_PATH, TESSERACT_PATH
import pytesseract
import io
import base64

pytesseract.pytesseract.tesseract_cmd = '{}{}'.format(settings.BASE_DIR,
                                                      TESSERACT_PATH)

stopwords = set(STOPWORDS)


def pdf_to_image(pdf_obj):
    images = convert_from_bytes(pdf_obj.read(),
                            poppler_path='{}{}'.format(settings.BASE_DIR,
                                                       POPPLER_PATH))

    return images


def ocr(images):
    text = ""
    for page in images:
        text += str(pytesseract.image_to_string(page))

    return text


def create_word_cloud(text):
    wordcloud = WordCloud(width=800, height=800,
                          colormap="Oranges_r",
                          stopwords=stopwords,
                          min_font_size=10).generate(text)

    img = wordcloud.to_image()

    return img

from django.shortcuts import render

# Create your views here.

def pdf_upload_view(request):
    """
    PDF upload page
    :param request:
    :return: page_title
    """
    page_title = "PDF upload"
    return render(request, 'pdf_upload.html', {'page_title': page_title})

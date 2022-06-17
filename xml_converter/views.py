from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from xml_converter.utils import xml_to_dict
from xml.etree.ElementTree import ParseError
import logging

def upload_page(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['file']
            json_data = xml_to_dict(uploaded_file)
        except (FileNotFoundError, ParseError) as e:
            logging.error(e)
            return HttpResponseBadRequest('An error Ocurred. Unexpected file format or File not found', status=404)
        return JsonResponse(json_data)

    return render(request, "upload_page.html")
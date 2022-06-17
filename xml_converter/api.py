from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml.etree.ElementTree import ParseError
from xml_converter.utils import xml_to_dict
import logging


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        try:
            uploaded_file = request.data['file']
            json_data = xml_to_dict(uploaded_file)
        except (FileNotFoundError, ParseError) as e:
            logging.error(e)
            return Response({'error': 'An error Ocurred. Unexpected file format or File not found'})
        return Response(json_data)

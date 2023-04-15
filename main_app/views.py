from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Ads
from .serializers import AdsSerializer


@api_view(['GET'])
def ads_list_api_view(request):
    ads_list = Ads.objects.all()
    ads_json = AdsSerializer(instance=ads_list, many=True).data

    return Response(data=ads_json)


@api_view(['GET'])
def test_api_view(request):
    data_dict = {
        'text': 'Hello World',
        'int': 1000,
        'float': 2.5,
        'bool': True,
        'dict': {'key': 'value'}
    }
    return Response(data=data_dict, status=status.HTTP_303_SEE_OTHER)

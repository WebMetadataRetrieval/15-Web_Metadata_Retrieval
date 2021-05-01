from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import F

from .serializers import MetadataSerializer
from Account.models import UserAccount
from Metadata.models import Metadata
from Metadata.scrapper import scrapper

@api_view(['GET',])
def metadata_api(request):
    if request.method == "GET":

        if not 'web_page' in request.GET:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not 'api_key' in request.GET:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
        web_page = request.GET['web_page']
        api_key = request.GET['api_key']

        try:
            client = UserAccount.objects.get(api_key=api_key)
        except UserAccount.DoesNotExist:
            res = {}
            res['reason'] = "Invalid API Key"
            return Response(res, status=status.HTTP_401_UNAUTHORIZED)
        
        if client.daily_limit < 1:
            res = {}
            res['reason'] = "Daily Limit Exceeded"
            return Response(res, status=status.HTTP_403_FORBIDDEN)

        client.daily_limit = F('daily_limit') - 1
        client.save()

        cached = 'true'
        if 'cached' in request.GET:
            cached = request.GET['cached']

        if cached=='true' or cached=='True':
            try:
                response = Metadata.objects.get(web_page=web_page)
                serialized_res = MetadataSerializer(response)
                return Response(serialized_res.data, status=status.HTTP_200_OK)
            except Metadata.DoesNotExist:
                pass

        # res = {}
        # res['web_page'] = web_page
        # res['api_key'] = api_key
        # res['cached'] = cached
        # return Response(res, status=status.HTTP_200_OK)

        # Call Scrapper
        response = scrapper.retrive_metadata(web_page)

        # Cache Response
        response.save()

        # Return Response
        serialized_res = MetadataSerializer(response)
        return Response(serialized_res.data, status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

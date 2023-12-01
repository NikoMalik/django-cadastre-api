from re import I
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models  import QueryHistory 
from rest_framework.decorators import api_view
from .models import QueryHistory
from .serializers import QueryHistorySerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import ParseError
@csrf_exempt
def query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cadastre_number = data.get('cadastre number')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
    
            external_server_response = True
            QueryHistory.objects.create(
                cadastre_number=cadastre_number,
                latitude=latitude,
                longitude=longitude,
                external_server_response=external_server_response
            )
            return JsonResponse({'result': 'Query received'})
        except ParseError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method. Use POST.'})

def result(request):
    return JsonResponse({'message': 'This is the result endpoint.'})

def ping(request):
    return JsonResponse({'message': 'Pong! The server is up and running.'})
@api_view(['GET'])
def history(request):
    if request.method == 'GET':
       
        all_queries = QueryHistory.objects.all()
        serialazer = QueryHistorySerializer(all_queries, many=True)
       

        return JsonResponse(serialazer.data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method. Use GET.'})
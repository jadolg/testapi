import json

from django.core.mail import EmailMessage
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST', 'GET'])
def ping(request):
    if request.method == 'POST':
        txt = json.dumps(request.data)
        email = EmailMessage("databack", txt, to=["diazorozcoj@gmail.com", ])
        email.send()
        return Response({'status': 'ok', 'data':request.data})
    elif request.method == 'GET':
        return Response({'status': 'ok'})
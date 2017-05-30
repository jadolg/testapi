import json

from django.core.mail import EmailMessage
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST', 'GET'])
def ping(request):
    if request.method == 'POST':
        body = ''
        if request.data.get('plain') != '':
            body = request.data.get('plain')
        elif request.data.get('html') != '':
            body = request.data.get('html')

        data = {'subject': request.data.get('headers[Subject]'),
                'body': body,
                'from': request.data.get('envelope[from]')}

        email = EmailMessage('databack', json.dumps(data), to=[data['from'], ])
        email.send()
        return Response({'status': 'ok', 'data': request.data})
    elif request.method == 'GET':
        return Response({'status': 'ok'})

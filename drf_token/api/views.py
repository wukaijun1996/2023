from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class BookView(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    def get(self, request):
        return Response('ok')

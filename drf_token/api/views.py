from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from api.auth import MyToken


class BookView(APIView):
    # authentication_classes = [JSONWebTokenAuthentication, ]
    authentication_classes = [MyToken, ]

    def get(self, request):
        print(request.user)
        return Response('ok')

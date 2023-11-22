from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from luffyapi.utils.response import APIResponse

# from luffyapi.utils.exceptions import


class TestView(APIView):
    def get(self, *args, **kwargs):
        dic = {'name': 'wkj'}
        print(dic['age'])
        return APIResponse()

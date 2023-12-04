from django.shortcuts import render, HttpResponse

# Create your views here.

from rest_framework.views import APIView
from luffyapi.utils.response import APIResponse


# from luffyapi.utils.exceptions import


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        dic = {'name': 'wkj'}
        # print(dic['age'])
        print('xxxxxxxxxxxxx')
        return APIResponse(headers={'Access-Control-Allow-Origin': '*'})


def test(request):
    print(request.method)
    res = HttpResponse('ok')
    # res['Access-Control-Allow-Origin'] = '*'
    # if request.method == "OPTIONS":
    #     res["Access-Control-Allow-Headers"] = "Content-Type"
    return res

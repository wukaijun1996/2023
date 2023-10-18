from django.shortcuts import render, HttpResponse
from rest_framework.viewsets import ModelViewSet
from app01.models import Book
from app01.ser import BookModelSerializer

from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


# Create your views here.
class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class Books(View):
    # 如果有个需求，只能接受get请求
    # http_method_names = ['get', ]
    def get(self, request):
        return HttpResponse("ok")


class BooksAPIView(APIView):
    # 如果有个需求，只能接受get请求
    # http_method_names = ['get', ]
    def get(self, request):
        # print(request.data)
        print(request.method)
        print(request.query_params)
        return HttpResponse("ok")

    def post(self, request):
        print(request.data)
        print(request.POST)
        print(request._request.POST)

        return HttpResponse("ok")

from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from app04.models import Book
from app04.ser import BookSerializer
from rest_framework.decorators import action  # 装饰器


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # method 第一个参数 传一个列表，列表中放请求方式
    # detail 布尔类型 当为True时需要传pk
    @action(methods=['GET','post'], detail=False)
    def get_11(self, request):
        book = self.get_queryset()[:2]  # 从1开始截取2条
        ser = self.get_serializer(book, many=True)

        return Response(ser.data)

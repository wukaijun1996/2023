from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from api import models
from api.ser import BookModelSerializer
from rest_framework.views import APIView


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 查询单个和查询所有 合到一起
        book_list = models.Book.objects.all().filter(is_delete=False)
        book_list_ser = BookModelSerializer(book_list, many=True)
        return Response(data=book_list_ser.data)

    def post(self, request, *args, **kwargs):
        book_ser = BookModelSerializer(data=request.data)
        book_ser.is_valid(raise_exception=True)
        book_ser.save()
        return Response(data=book_ser.data)


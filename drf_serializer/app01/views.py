from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from rest_framework.views import APIView
from app01.models import Book
from app01.ser import BookSerializer, BookModelSerializer
from rest_framework.response import Response

from app01.utils import MyResponse


class BookView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(id=pk).first()
        book_ser = BookSerializer(instance=book)
        #  系列化对象.data 就是序列化后的字典
        return Response(book_ser.data)
        # return JsonResponse(book_ser.data)

    def put(self, request, pk):
        response_msg = {"status": 100, "msg": "成功"}
        # 找到这个对象
        book = Book.objects.filter(id=pk).first()
        # 得到一个序列化类的对象
        book_ser = BookSerializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg["data"] = book_ser.data
        else:
            response_msg["status"] = 101
            response_msg["msg"] = "数据校验失败"
            response_msg["data"] = book_ser.errors

        return Response(response_msg)

    def delete(self, request, pk):
        response = MyResponse()
        ret = Book.objects.filter(pk=pk).delete()
        return Response(response.get_dict)


class BooksView(APIView):
    def get(self, request):
        response = MyResponse()
        books = Book.objects.all()
        books_ser = BookSerializer(books, many=True)  # 序列化多条,如果序列化一条，不需要写
        response.data = books_ser.data
        return Response(response.get_dict)

    # 新增
    def post(self, request):
        response_msg = {"status": 100, "msg": "成功"}
        # 修改才有instance 新增没有instance 只有data
        book_ser = BookSerializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            response_msg["data"] = book_ser.data
        else:
            response_msg["status"] = 102
            response_msg["msg"] = "数据校验失败"
            response_msg["data"] = book_ser.errors
        return Response(response_msg)


class BooksView2(APIView):
    def get(self, request):
        response = MyResponse()
        books = Book.objects.all()
        book = Book.objects.all().first()
        books_ser = BookModelSerializer(books, many=True)  # 序列化多条,如果序列化一条，不需要写
        book_one_ser = BookModelSerializer(book)  # 序列化多条,如果序列化一条，不需要写
        print(type(books_ser))
        print(type(book_one_ser))
        response.data = books_ser.data  # 自定义字典增加键值对
        return Response(response.get_dict)

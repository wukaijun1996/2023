from django.shortcuts import render

# Create your views here.

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.renderers import JSONRenderer


class TestView(APIView):
    # 局部配置 ，只对TestView有效,接口中只返回json数据
    renderer_classes = [JSONRenderer, ]

    def get(self, request):
        print(request)
        return Response({'name': 'lqz'}, status=status.HTTP_200_OK, headers={'token': 'xxx'})


class TestView2(APIView):
    def get(self, request):
        print(request)
        return Response({'name': '2222'}, status=status.HTTP_200_OK, headers={'token': 'xxx'})


# ###############################################视图相关


from rest_framework.generics import GenericAPIView
from app03.models import Book
from app03.ser import BookSerializer


# 基于APIView 写的
class BookView(APIView):
    def get(self, request):
        book_list = Book.objects.all()
        book_ser = BookSerializer(book_list, many=True)
        return Response(book_ser.data)

    def post(self, request):
        book_ser = BookSerializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})


class BookDetailView(APIView):
    def get(self, request, pk):
        book = Book.objects.all().filter(pk=pk).first()
        book_ser = BookSerializer(book)
        return Response(book_ser.data)

    def put(self, request, pk):
        book = Book.objects.all().filter(pk=pk).first()
        book_ser = BookSerializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})

    def delete(self, request, pk):
        ret = Book.objects.filter(pk=pk).delete()
        return Response({'status': 100, 'msg': '删除成功'})


# GenericAPIView 写的
class Book2View(GenericAPIView):
    # queryset 要传queryset对象 ，查询了所有的图书
    # serializer_class 使用哪个序列化类来序列化这堆数据
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        book_list = self.get_queryset()
        book_ser = self.get_serializer(book_list, many=True)
        return Response(book_ser.data)

    def post(self, request):
        book_ser = self.get_serializer(data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})


class Book2DetailView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk):
        book = self.get_object()
        book_ser = self.get_serializer(book)
        return Response(book_ser.data)

    def put(self, request, pk):
        book = self.get_object()
        book_ser = self.get_serializer(instance=book, data=request.data)
        if book_ser.is_valid():
            book_ser.save()
            return Response(book_ser.data)
        else:
            return Response({'status': 101, 'msg': '校验失败'})

    def delete(self, request, pk):
        ret = self.get_object().delete()
        return Response({'status': 100, 'msg': '删除成功'})


# 五个mixins视图扩展类写法，比上面更简洁
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin


class Book3View(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Book3DetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)


# GenericAPIView的视图子类9个   更更简洁
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView


class Book4View(ListAPIView, CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Book4DetailView(UpdateAPIView, RetrieveAPIView, DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 使用ModelViewSet 编写5个接口
from rest_framework.viewsets import ModelViewSet


class Book5View(ModelViewSet):  # 5个接口都有，但是路由有点问题
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 直接继承ViewSetMixin， 配置路由执行自定义get_all_book方法
from rest_framework.viewsets import ViewSetMixin


class Book6View(ViewSetMixin, APIView):
    def get_all_book(self, request):
        book_list = Book.objects.all()
        book_ser = BookSerializer(book_list, many=True)

        return Response(book_ser.data)

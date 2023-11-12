from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response

from api import models
from api.ser import BookModelSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 查询单个和查询所有 合到一起
        # 查单个
        if kwargs.get('pk', None):
            book = models.Book.objects.filter(pk=kwargs.get('pk')).first()
            if book:
                book_ser = BookModelSerializer(book)
                return Response(data=book_ser.data)
            else:
                return Response({'msg': '查询数据不存在'})
        else:
            # 查所有
            book_list = models.Book.objects.all().filter(is_delete=False)
            book_list_ser = BookModelSerializer(book_list, many=True)
            return Response(data=book_list_ser.data)

    def post(self, request, *args, **kwargs):
        # 具备增单条 和增多条的功能
        if isinstance(request.data, dict):
            book_ser = BookModelSerializer(data=request.data)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
        elif isinstance(request.data, list):
            # 现在book_ser是ListSerializer对象
            book_ser = BookModelSerializer(data=request.data, many=True)  # 增多条
            print(type(book_ser))
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            # 新增--》ListSerializer---> create方法
            # def create(self, validated_data):
            # self.child是BookModelSerializer
            #     return [
            #         self.child.create(attrs) for attrs in validated_data
            #     ]
            return Response(data=book_ser.data)

    def put(self, request, *args, **kwargs):
        # 改一个 改多个
        # 改一个
        if kwargs.get('pk', None):
            book = models.Book.objects.filter(pk=kwargs.get('pk')).first()
            book_ser = BookModelSerializer(instance=book, data=request.data, partial=True)  # partial 可以改一部分
            print(type(book_ser))
            book_ser.is_valid(raise_exception=True)
            book_ser.save()
            return Response(data=book_ser.data)
        else:
            # 前端数据  [{id:1,name:xx,price:xx},{id:1,name:xx,price:xx}]
            # 处理传入的数据 对象列表 修改的数据列表
            book_list = []
            modify_data = []
            for item in request.data:
                print(item)
                pk = item.pop('id')
                book = models.Book.objects.get(pk=pk)
                book_list.append(book)
                modify_data.append(item)
            # 第一种方案 for循环一个一个修改
            # for i, si_data in enumerate(modify_data):
            #     book_ser = BookModelSerializer(instance=book_list[i], data=si_data)
            #     book_ser.is_valid(raise_exception=True)
            #     book_ser.save()
            # return Response({'msg': '成功'})
            # 第二种方案 重写ListSerializer的update方法
            book_ser = BookModelSerializer(instance=book_list, data=modify_data, many=True)
            book_ser.is_valid(raise_exception=True)
            book_ser.save()  # ListSerializer的update方法,自己写的update方法

            return Response(book_ser.data)

    def delete(self, request, *args, **kwargs):
        # 单个删
        pk = kwargs.get('pk')
        pks = []
        if pk:
            pks.append(pk)
        else:
            # 多条删除 {'pks':[1,2,3}
            pks = request.data.get('pks')
        ret = models.Book.objects.filter(pk__in=pks, is_delete=False).update(is_delete=True)
        print(ret)
        if ret:
            return Response(data={'msg': '删除成功'})
        else:
            return Response(data={'msg': '没有要删除的数据'})


# 查所有 才需要分页
# 内置三种分页方式
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from utils.throttling import MyThrottle

"""
PageNumberPagination
    page_size:每页显示的页数
"""


class MyPageNumberPagination(PageNumberPagination):
    page_size = 3  # 每页条数  http://127.0.0.1:8080/api/books2/?aaa=1&size=6
    page_query_param = 'aaa'  # 查询第几页的key
    page_size_query_param = 'size'  # 每一页显示的条数
    max_page_size = 5  # 每页最大显示条数


class BookView(ListAPIView):
    throttle_classes = [MyThrottle, ]
    queryset = models.Book.objects.filter()
    serializer_class = BookModelSerializer
    # 配置分页
    pagination_class = MyPageNumberPagination


# 自定制的频率限制类
class MtThrottle():
    pass



















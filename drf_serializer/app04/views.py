from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from app04.models import Book
from app04.ser import BookSerializer
from rest_framework.decorators import action  # 装饰器
from rest_framework.views import APIView
from rest_framework.response import Response
from app04 import models

from app04.app_auth import MyAuthentication, UserPermission


class BookViewSet(ModelViewSet):
    authentication_classes = [MyAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # method 第一个参数 传一个列表，列表中放请求方式
    # detail 布尔类型 当为True时需要传pk
    @action(methods=['GET', 'post'], detail=False)
    def get_11(self, request):
        print(request.user.username)
        print(request.user.password)
        book = self.get_queryset()[:2]  # 从1开始截取2条
        ser = self.get_serializer(book, many=True)

        return Response(ser.data)


class TestView(APIView):
    from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
    # authentication_classes = [MyAuthentication, ]
    # permission_classes = [UserPermission, ]
    # throttle_classes = [AnonRateThrottle, ]

    def get(self, request):
        print(request.user)
        print(request.auth)
        return Response({'msg': '我是测试'})


from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication


class Test1View(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser, ]

    def get(self, request):
        print(request.user)
        print(request.auth)
        return Response({'msg': '超级管理有能看'})


from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


# 过滤组件的使用
class BookView(ListAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, ]
    # 过滤某个字段
    filterset_fields = ['name', 'price', ]


from rest_framework.filters import OrderingFilter


# 排序组件的使用  (使用时用 ordering=-price&&ordering=-id)
class Book2View(ListAPIView):
    queryset = Book.objects
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter, ]
    # 排序某个字段
    ordering_fields = ['id', 'price', ]


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        print(password)
        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            # 登陆成功,生成一个随机字符串
            import uuid
            token = uuid.uuid4()
            # 存到UserToken表中
            # models.UserToken.objects.create(token=token, user=user)
            # 跨表查询
            # user1 = models.UserToken.objects.filter(user__username=username).first()
            # print(user1.user.get_user_type_display())

            models.UserToken.objects.update_or_create(defaults={'token': token}, user=user)  # 查得到，update 查不到，create
            return Response({'status': 100, 'msg': '登陆成功', 'token': token})
        else:
            return Response({'status': 101, 'msg': '用户名或密码错误'})


# 频率限制
from rest_framework.throttling import BaseThrottle

# 认证 权限 频率 过滤 排序都在这

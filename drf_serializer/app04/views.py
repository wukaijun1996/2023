from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from app04.models import Book
from app04.ser import BookSerializer
from rest_framework.decorators import action  # 装饰器
from rest_framework.views import APIView
from rest_framework.response import Response
from app04 import models

from app04.app_auth import MyAuthentication


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
    def get(self, request):
        print(request.user)
        print(request.auth)
        return Response({'msg': '我是测试'})


class LoginView(APIView):
    authentication_classes = []

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

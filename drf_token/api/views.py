from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from api.auth import MyToken


class BookView(APIView):
    # authentication_classes = [JSONWebTokenAuthentication, ]
    authentication_classes = [MyToken, ]

    def get(self, request):
        print(request.user)
        return Response('ok')


# 内置权限类
from rest_framework.permissions import IsAuthenticated


# 可以通过认证类JSONWebTokenAuthentication和权限类IsAuthenticated来控制用户登录以后才能访问某些接口
# 如果用户不登录就可以访问 去掉权限类就ok
class OrderAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]  # 权限控制 需要有user 并且通过认证

    def get(self, request, *args, **kwargs):
        return Response('这是订单信息')


class UserInfoAPIView(APIView):
    authentication_classes = [JSONWebTokenAuthentication, ]

    # permission_classes = [IsAuthenticated, ] # 不加 游客可以登录往下走

    def get(self, request, *args, **kwargs):
        return Response('UserInfoAPIView')


# 自动签发token 完成多方式登录
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, ViewSet
from api.ser import LoginModelSerializer


# class Login2View(ViewSetMixin,APIView):
class Login2View(ViewSet):
    def login(self, request, *args, **kwargs):
        login_ser = LoginModelSerializer(data=request.data, context={'request': request})

        login_ser.is_valid(raise_exception=True)
        token = login_ser.context.get('token')

        return Response({'status': 100, 'msg': '登录成功', 'token': token, 'username': login_ser.context.get('username')})

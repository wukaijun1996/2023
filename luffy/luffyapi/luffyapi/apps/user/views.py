from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ViewSet
from user import serializaer
from luffyapi.utils.response import APIResponse
from rest_framework.decorators import action
from user import models
from user.throttings import SMSThrottling


class LoginView(ViewSet):
    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        """
        手机号登录，邮箱登录，用户名 多登陆接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ser = serializaer.UserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)

    @action(methods=['GET'], detail=False)
    def check_telephone(self, request, *args, **kwargs):
        """
        检查手机号接口（手机号登录，需要检查手机号是否在数据库是否存在及合法）
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        import re
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        try:
            models.User.objects.get(telephone=telephone)
            return APIResponse(code=1)
        except:
            return APIResponse(code=0, msg='手机号不存在')

    @action(methods=['POST'], detail=False)
    def code_login(self, request, *args, **kwargs):
        """
        验证码登录接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ser = serializaer.CodeUserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)


class SendSmsView(ViewSet):
    throttle_classes = [SMSThrottling, ]

    @action(methods=['GET'], detail=False)
    def send(self, request, *args, **kwargs):
        """
        发送验证码接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        import re
        from luffyapi.lib.tx_sms.send import get_code, send_message
        from django.core.cache import cache
        from django.conf import settings
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}$', telephone):
            return APIResponse(code=0, msg='手机号不合法')
        code = get_code()
        result = send_message(telephone, code)
        print(result)
        cache.set(settings.PHONE_CACHE_KEY % telephone, code, 180)
        if result:
            return APIResponse(code=1, msg='验证号发送成功')
        else:
            return APIResponse(code=0, msg='验证号发送失败')

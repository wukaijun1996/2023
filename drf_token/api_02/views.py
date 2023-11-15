from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from api_02 import models
from api_02.ser import UserModelserializer, UserReadOnlyModelserializer, UserImageModelserializer


class RegisterView(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = UserModelserializer

    # 假设get请求和post请求，用的序列化类不一样，重写get_serializer_class,返回啥，用的序列化类就是啥
    # 注册用的UserModelserializer，查询一个人用的序列化类是UserReadOnlyModelserializer
    def get_serializer_class(self):
        print(self.action)  # create ,retrieve
        if self.action == 'create':
            return UserModelserializer
        elif self.action == 'retrieve':
            return UserReadOnlyModelserializer
        elif self.action == 'update':
            return UserImageModelserializer
        else:
            return self.serializer_class

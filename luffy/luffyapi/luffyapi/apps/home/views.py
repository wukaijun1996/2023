from django.shortcuts import render, HttpResponse

# Create your views here.

from rest_framework.views import APIView
from luffyapi.utils.response import APIResponse
from luffyapi.utils.logger import log

from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from home import models
from home import serializaer

from django.conf import settings


# class BannerView(GenericAPIView, ListModelMixin): 路由配置 path('banner/', views.BannerView.as_view())
class BannerView(GenericViewSet, ListModelMixin):  # 路由配置
    # 无论有多少待展示的数据，最多就展示3条
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[
               :settings.BANNER_COUNTER]
    serializer_class = serializaer.BannerModelSerializer

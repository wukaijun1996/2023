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
from django.core.cache import cache
from rest_framework.response import Response


# class BannerView(GenericAPIView, ListModelMixin): 路由配置 path('banner/', views.BannerView.as_view())
class BannerView(GenericViewSet, ListModelMixin):  # 路由配置
    # 无论有多少待展示的数据，最多就展示3条
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')[
               :settings.BANNER_COUNTER]
    serializer_class = serializaer.BannerModelSerializer

    def list(self, request, *args, **kwargs):
        # 把data的数据加缓存
        # 1.先去缓存拿数据
        banner_list = cache.get('banner_list')
        print('giao')
        if not banner_list:
            print('to redis')
            response = super().list(request, *args, **kwargs)
            # 加到缓存
            cache.set('banner_list', response.data, 60 * 60 * 24)
            return response
        return Response(data=banner_list)

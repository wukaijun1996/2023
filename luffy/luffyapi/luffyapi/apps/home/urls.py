from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

from luffyapi.apps.home import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('banner', views.BannerView, 'banner')

urlpatterns = [
    # path('banner/', views.BannerView.as_view())
    path('', include(router.urls))
]

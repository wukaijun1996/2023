"""drf_token URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework_jwt.views import ObtainJSONWebToken, VerifyJSONWebToken, RefreshJSONWebToken, obtain_jwt_token
from api import views
from django.views.static import serve  # django内置给你的视图函数
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    path('books/', views.BookView.as_view()),
    path('order/', views.OrderAPIView.as_view()),
    path('userinfo/', views.UserInfoAPIView.as_view()),

    # 缓存
    path('test/', views.test_cache1),
    path('test2/', views.test_cache2),

    # 多方式登录签发token
    path('login2/', views.Login2View.as_view(actions={'post': 'login'})),

    path('api_02/', include('api_02.urls')),
    # 开放media文件夹
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}, name="media"),

]

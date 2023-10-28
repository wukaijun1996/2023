"""drf_serializer URL Configuration

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

from django.urls import path, re_path, include
from app03 import views

urlpatterns = [
    path(r'test/', views.TestView.as_view()),
    path(r'test2/', views.TestView2.as_view()),
    path(r'books/', views.BookView.as_view()),
    re_path(r'books/(?P<pk>\d+)', views.BookDetailView.as_view()),

    # 使用GenericAPIView重写的
    path(r'books2/', views.Book2View.as_view()),
    re_path(r'books2/(?P<pk>\d+)', views.Book2DetailView.as_view()),

    # 使用mixins视图扩展类重写
    path(r'books3/', views.Book3View.as_view()),
    re_path(r'books3/(?P<pk>\d+)', views.Book3DetailView.as_view()),

    # 使用GenericAPIView的视图子类(9个) 重写
    path(r'books4/', views.Book4View.as_view()),
    re_path(r'books4/(?P<pk>\d+)', views.Book4DetailView.as_view()),

    # 使用ModelViewSet编写5个接口
    # 当路径匹配，又是get请求，会执行Book5View的list方法
    path(r'books5/', views.Book5View.as_view(actions={'get': 'list', 'post': 'create'})),
    re_path(r'books5/(?P<pk>\d+)',
            views.Book5View.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # 直接继承ViewSetMixin， 配置路由执行自定义get_all_book方法
    path(r'books6/', views.Book6View.as_view(actions={'get': 'get_all_book'})),
]

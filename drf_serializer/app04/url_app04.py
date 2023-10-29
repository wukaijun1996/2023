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
from app04 import views

# 导入routers  模块
from rest_framework import routers

# routers有两个类
# routers.DefaultRouter 生成的路由更多
# routers.SimpleRouter
router = routers.SimpleRouter()
# 注册
# route.register('前缀', '继承ModelViewSet的视图类', '别名')
router.register('books', views.BookViewSet)
# route.urls 自动生成的路由
print(router.urls)

urlpatterns = [
    path(r'books/', views.BookViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    re_path(r'books/(?P<pk>\d+)',
            views.BookViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # 登录LoginView
    path(r'login/', views.LoginView.as_view()),
    path(r'test/', views.TestView.as_view()),

]

urlpatterns += router.urls

"""
app04/ ^books/$ [name='book-list']  跟simple一样
app04/ ^books\.(?P<format>[a-z0-9]+)/?$ [name='book-list']
app04/ ^books/(?P<pk>[^/.]+)/$ [name='book-detail']   # 跟simple一样
app04/ ^books/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='book-detail']
app04/ ^$ [name='api-root']  根  返回 所有可以返回的地址
app04/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
"""


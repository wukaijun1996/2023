
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from luffyapi.apps.home import views


urlpatterns = [
    # path('admin/', admin.site.urls),

    # media文件夹路径开放
    # path('home/', views.TestView.as_view())
    path('home/', views.test)

]

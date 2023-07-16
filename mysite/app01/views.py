from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 去app目录下的templates目录寻找user_list.html，根据app的注册顺序，逐一去他们的templates目录中找
    return render(request, "user_list.html")


def user_add(request):
    return HttpResponse("添加用户")

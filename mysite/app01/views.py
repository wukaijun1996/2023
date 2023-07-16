from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 去app目录下的templates目录寻找user_list.html，根据app的注册顺序，逐一去他们的templates目录中找
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name = "1234"
    roles = ['管理员', 'CEO', '保安', '打工人']
    data_list = [
        {"name": "高启强", "role": "QA", "salary": 3000},
        {"name": "安欣", "role": "CEO", "salary": 2000},
        {"name": "高育良", "role": "employee", "salary": 8000},
    ]
    return render(request, 'tpl.html', {"n1": name, 'n2': roles, 'n3': data_list})


def news(request):
    import requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2023/07/news",
                       headers=headers)
    data_list = res.json()
    print(data_list)

    return render(request, "news.html", {"news_list": data_list})


def something(request):
    # request是一个对象，封装了 用户发送过来的所有请求相关数据

    print(request.method)

    return HttpResponse("返回内容")

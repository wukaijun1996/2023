from django.shortcuts import render, HttpResponse, redirect


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

    # 1.获取请求方式
    print(request.method)
    # 2.在URL上传递值
    print(request.GET)
    # 3.在请求体中提交数据
    print(request.POST)
    # 4.HttpResponse（‘返回内容'）
    #   return HttpResponse("返回内容")
    # 5.读取HTML的内容  + 渲染（替换） ->字符串，返回给用户浏览器
    # return render(request, "user_list.html")
    # 6.让浏览器重定向到其他的页面
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        print(request.POST.get('user'))
        print(request.POST.get('pwd'))
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username == 'root' and password == "123456":
            return HttpResponse("登陆成功")
        else:
            # return HttpResponse("登录失败")
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})

    # return render(request, 'login.html')

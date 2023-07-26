from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from app02.models import Admin
from app02.utils.bootstrap import BootStrapForm
from django.core.exceptions import ValidationError
from app02.utils.encrypt import md5


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}, render_value=True)
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        # forms.Form 只能返回输入后的数据form.cleaned_data
        print(form.cleaned_data)
        # admin_object = Admin.objects.filter(username=form.cleaned_data.get("username"),
        #                                     password=md5(form.cleaned_data.get("password"))).first()
        admin_object = Admin.objects.filter(**form.cleaned_data).first()
        print(admin_object)
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, "login.html", {"form": form})

        # 用户名和密码正确
        # 网站生成随机字符串，写到用户浏览器的cookie中，再写入到session中
        request.session["info"] = {"id": admin_object.id, "name": admin_object.username}
        return redirect("/admin/list")

    return render(request, "login.html", {"form": form})

def loginout(request):
    """注销"""
    request.session.clear()
    return redirect("/login/")

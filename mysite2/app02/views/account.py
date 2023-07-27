from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from app02.models import Admin
from app02.utils.bootstrap import BootStrapForm
from django.core.exceptions import ValidationError
from app02.utils.encrypt import md5
from app02.utils.code import check_code
from io import BytesIO


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}, render_value=True)
    )

    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
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
        # 拿到输入的验证码的值
        user_input_code = form.cleaned_data.pop("code")
        # 后端生成的真正的图片的值
        code = request.session.get("image_code", "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, "login.html", {"form": form})

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
        # session保存七天免登录
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/admin/list")

    return render(request, "login.html", {"form": form})


def image_code(request):
    """生成图片验证码"""
    # 调用pillow函数，生成图片
    img, code_string = check_code()
    # 写入到自己的session中（以便后续获取验证码再进行校验）
    request.session["image_code"] = code_string
    # 给session设置60s超时
    request.session.set_expiry(60)
    # print(code_string)

    # 将生成的图片保存在缓存中
    stream = BytesIO()
    img.save(stream, "png")

    return HttpResponse(stream.getvalue())


def loginout(request):
    """注销"""
    request.session.clear()
    return redirect("/login/")

from django.shortcuts import render, redirect
from app02.models import Admin
from app02.utils.pagination import Pagination


def admin_list(request):
    """管理员列表"""

    # 搜索框
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["username__contains"] = search_data

    queryset = Admin.objects.filter(**data_dict).all()

    # 分页
    page_object = Pagination(request, queryset)
    page_string = page_object.html()
    context = {
        "queryset": queryset,
        "page_string": page_string,
        "search_data": search_data,
    }

    return render(request, "admin_list.html", context)


from django import forms
from app02.utils.bootstrap import BootStrapModelForm
from django.core.exceptions import ValidationError
from app02.utils.encrypt import md5


class AdminModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        # render_value=True 两次输入不一致内容不清空
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        return md5(self.cleaned_data.get("password"))

    def clean_confirm_password(self):
        if self.cleaned_data.get("password") == md5(self.cleaned_data.get("confirm_password")):
            # 返回什么 此字段以后保存到数据库就是什么
            return md5(self.cleaned_data.get("confirm_password"))
        else:
            raise ValidationError("两次输入不一致")


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = Admin
        fields = ["username"]


class AdminResetModelForm(BootStrapModelForm):
    confirm_password = forms.CharField(
        label="确认密码",
        # render_value=True 两次输入不一致内容不清空
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = Admin
        fields = ["password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)
        # 去数据库校验当前密码和新输入的密码是否一致
        exists = Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("密码不能与之前相同")
        return md5_pwd

    def clean_confirm_password(self):
        # 钩子方法由上到下执行，此时password已加密
        if self.cleaned_data.get("password") == md5(self.cleaned_data.get("confirm_password")):
            # 返回什么 此字段以后保存到数据库就是什么
            return md5(self.cleaned_data.get("confirm_password"))
        else:
            raise ValidationError("两次输入不一致")


def admin_add(request):
    """添加管理员"""
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, "change.html", {"title": title, "form": form})

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)

        form.save()
        return redirect("/admin/list")

    return render(request, "change.html", {"title": title, "form": form})


def admin_edit(request, nid):
    """编辑管理员"""
    row_object = Admin.objects.filter(id=nid).first()
    if not row_object:
        redirect("/admin/list")
    title = "编辑管理员"
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, "change.html", {"title": title, "form": form})
    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list")
    return render(request, "change.html", {"title": title, "form": form})


def admin_delete(request, nid):
    """删除管理员"""

    Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list")


def admin_reset(request, nid):
    """重置密码"""
    row_object = Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect("/admin/list")
    title = "重置密码 - {}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, "change.html", {"form": form, "title": title})
    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/admin/list")
    return render(request, "change.html", {"form": form, "title": title})

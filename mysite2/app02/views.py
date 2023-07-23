from django.shortcuts import render, HttpResponse, redirect
from app02.models import Department, UserInfo, PrettyNum
from django.utils.safestring import mark_safe
from app02.utils.pagination import Pagination

# Create your views here.

def depart_list(request):
    """部门列表"""
    queryset = Department.objects.all()
    print(queryset)
    return render(request, "depart_list.html", {"queryset": queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, "depart_add.html")
    Department.objects.create(title=request.POST.get('title'))
    return redirect("/depart/list")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get('nid')
    Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")


def depart_edit(request, nid):
    """编辑部门"""
    if request.method == "GET":
        depart = Department.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {"depart": depart.title})
    Department.objects.filter(id=nid).update(title=request.POST.get("title"))
    return redirect("/depart/list")


def user_list(request):
    """用户列表"""
    queryset = UserInfo.objects.all()
    page_object = Pagination(request, queryset, page_size=3)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    # for obj in queryset:
    # print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display())
    # print(obj.name, obj.depart_id, obj.depart.title)
    # obj.depart_id # 获取数据库中存储的那个字段值
    # obj.depart # 根据id自动去关联的表中获取那一行数据depart的对象

    return render(request, "user_list.html", context)


def user_add(request):
    """添加用户"""
    if request.method == "GET":
        context = {
            "gender_choice": UserInfo.gender_choice,
            "depart_list": Department.objects.all(),
        }
        return render(request, "user_add.html", context)
    # 获取用户提交的数据
    name = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    account = request.POST.get("ac")
    create_time = request.POST.get("ctime")
    gender = request.POST.get("gender")
    depart_id = request.POST.get("dp")
    UserInfo.objects.create(name=name, password=password, age=age, account=account, create_time=create_time,
                            gender=gender, depart_id=depart_id)
    return redirect("/user/list")


# ModelForm示例 #############################
"""
ModelForm 针对数据库中的某个表
Form 
"""

from django import forms


class UserModelForm(forms.ModelForm):
    # 校验规则重写数据库的字段属性
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.TextInput(attrs={"class": "form-control"}),
        #     "age": forms.TextInput(attrs={"class": "form-control"}),
        # }
        # 上述方法麻烦，重写初始化方法(为了给输入框加样式)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # print(name, name == "password")
            # 当name为字段password,不设置样式
            # if str(name) == "password":
            #     continue
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_modelform_add(request):
    """添加用户 基于(ModelForm版本)"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "user_modelform_add.html", {"form": form})

    # 用户post提交数据
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        # print(form.cleaned_data)
        form.save()
        return redirect("/user/list/")

    # print(form.errors)
    return render(request, "user_modelform_add.html", {"form": form})


def user_edit(request, nid):
    """编辑用户"""
    row_object = UserInfo.objects.filter(id=nid).first()
    print(row_object)
    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据（对象）
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {"form": form})
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据， 如果想要在用户输入以外增加一点值(相当于设置改后是的默认值)
        # form.instance.字段名= 值
        # form.instance.name = "giao"
        form.save()
        return redirect("/user/list")

    return render(request, "user_edit.html", {"form": form})


def user_delete(request, nid):
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")


def pretty_list(request):
    """靓号列表"""

    # 搜索框
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["mobile__contains"] = search_data


    queryset = PrettyNum.objects.filter(**data_dict).order_by("-level")

    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    context = {
        "queryset": page_queryset,# 分完页的数据
        "search_data": search_data,
        "page_string": page_string  # 页码
    }
    return render(request, "pretty_list.html", context)


# ##############################################
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class PrettyModelForm(forms.ModelForm):
    # 校验手机号格式，必须按下面格式提交，不然不能提交
    # mobile = forms.CharField(
    #     label="手机号码",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    # )

    class Meta:
        model = PrettyNum
        # fields = ["mobile", "price", "level", "status"]
        # 要显示全部字段是也可以直接 add  "__all__"
        # 如果是除XX字段
        # exclude = ["level"]
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 钩子方法 校验手机号格式，必须按下面要求提交，不然不能提交
    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        print(self.instance.pk, "嘿嘿")
        # 获取用户传入的数据
        input_mobile = self.cleaned_data["mobile"]
        # 判断用户输入的手机号在数据库中是否已存在
        if PrettyNum.objects.filter(mobile=input_mobile).exists():
            raise ValidationError("手机号已存在1")
        if len(input_mobile) != 11:
            raise ValidationError("格式错误")
        return input_mobile


def pretty_add(request):
    """添加靓号"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, "pretty_add.html", {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list")
    return render(request, "pretty_add.html", {"form": form})


class PrettyEditModelForm(forms.ModelForm):
    # mobile = forms.CharField(disabled=True)

    class Meta:
        model = PrettyNum
        fields = ["mobile", "price", "level", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 钩子方法 校验手机号格式，必须按下面要求提交，不然不能提交
    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        print(self.instance.pk)
        # 获取用户传入的数据
        input_mobile = self.cleaned_data["mobile"]
        # 当编辑模式下校验号码是否存在 （exclude(id=self.instance.pk) 过滤掉自己）
        exists = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=input_mobile).exists()
        print(exists)
        if exists:
            raise ValidationError("手机号已存在")
        if len(input_mobile) != 11:
            raise ValidationError("格式错误")
        return input_mobile


def pretty_edit(request, nid):
    """编辑靓号"""
    row_object = PrettyNum.objects.filter(id=nid).first()
    # print(row_object)
    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_object)
        return render(request, "pretty_edit.html", {"form": form})
    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list")
    return render(request, "pretty_edit.html", {"form": form})


def pretty_delete(request, nid):
    PrettyNum.objects.filter(id=nid).delete()
    return redirect("/pretty/list")

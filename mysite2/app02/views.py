from django.shortcuts import render, HttpResponse, redirect
from app02.models import Department, UserInfo


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
    # for obj in queryset:
    # print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display())
    # print(obj.name, obj.depart_id, obj.depart.title)
    # obj.depart_id # 获取数据库中存储的那个字段值
    # obj.depart # 根据id自动去关联的表中获取那一行数据depart的对象

    return render(request, "user_list.html", {"queryset": queryset})


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

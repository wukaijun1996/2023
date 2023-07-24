from django.shortcuts import render, HttpResponse, redirect
from app02.models import Department, UserInfo, PrettyNum
from app02.utils.pagination import Pagination
from app02.utils.form import UserModelForm, PrettyModelForm, PrettyEditModelForm


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

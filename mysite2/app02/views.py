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

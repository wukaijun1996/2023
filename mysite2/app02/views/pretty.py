from django.shortcuts import render, HttpResponse, redirect
from app02.models import Department, UserInfo, PrettyNum
from app02.utils.pagination import Pagination
from app02.utils.form import UserModelForm, PrettyModelForm, PrettyEditModelForm



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
        "queryset": page_queryset,  # 分完页的数据
        "search_data": search_data,
        "page_string": page_string  # 页码
    }
    return render(request, "pretty_list.html", context)


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

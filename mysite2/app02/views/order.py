import random
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app02.models import Order
from app02.utils.bootstrap import BootStrapModelForm
from app02.utils.pagination import Pagination


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = Order
        # fields = "__all__"
        exclude = ["oid", "admin"]


def order_list(request):
    queryset = Order.objects.all().order_by("-id")
    page_object = Pagination(request, queryset, page_size=10)
    form = OrderModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, "order_list.html", context)


@csrf_exempt
def order_add(request):
    """新建订单（Ajax请求）"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # 固定设置管路员ID
        form.instance.admin_id = request.session["info"]["id"]
        form.save()
        return JsonResponse({"status": True})

    return JsonResponse({"status": False, "error": form.errors})


def order_delete(request):
    """删除订单"""
    uid = request.GET.get("uid")
    exists = Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "删除失败,数据不存在"})
    Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    """根据id获取订单信息"""
    uid = request.GET.get("uid")
    # .values("title", "price", "status")  从数据库中筛选找到对应数据 返回字典 {“title":1, "price":21}
    row_dict = Order.objects.filter(id=uid).values("title", "price", "status").first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})

    # 从数据库中获取到一个对象 row_object
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    """编辑订单"""
    uid = request.GET.get("uid")
    print(uid)
    row_object = Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在,刷新请重试"})
    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "error": form.errors})

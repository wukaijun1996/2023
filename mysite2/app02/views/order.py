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

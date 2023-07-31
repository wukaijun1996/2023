import json

from django.shortcuts import render, HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app02.utils.bootstrap import BootStrapModelForm
from app02.models import Task


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea
            "detail": forms.TextInput
        }


def task_list(request):
    """任务列表"""
    form = TaskModelForm()
    return render(request, "task_list.html", {"form": form})


@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    data_dict = {"status": "success", "data": [11, 22, 33, 44]}
    return JsonResponse(data_dict)


@csrf_exempt
def task_add(request):
    print(request.POST)

    # 1.用户发送过来的数据进行校验 （ModelForm进行校验）
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, "error": form.errors}

    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))

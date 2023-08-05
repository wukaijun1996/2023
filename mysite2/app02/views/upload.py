import os
from django import forms
from django.shortcuts import render, HttpResponse
from app02.utils.bootstrap import BootStrapForm, BootStrapModelForm
from app02.models import Boss, City
from django.conf import settings


def upload_list(request):
    if request.method == "GET":
        return render(request, "upload_list.html")
    # print(request.POST)  # 请求体中数据
    # print(request.FILES)  # 请求发过来的文件
    # print(request.FILES.get("avatar"))  # 请求发过来的某个文件对象
    print(request.FILES.get("avatar").name)  # 请求发过来的文件的名称
    # print(type(request.FILES.get("avatar")))  # 请求发过来的文件
    # print(type(request.FILES.get("avatar").name))  # 请求发过来的文件

    file_object = request.FILES.get("avatar")
    print(file_object.name)

    f = open(file_object.name, mode="wb")
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse("...")


class Upform(BootStrapForm):
    bootstrap_exclude_fields = ["img"]
    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


def upload_form(request):
    title = "Form上传"
    if request.method == "GET":
        form = Upform()
        return render(request, "upload_form.html", {"form": form, "title": title})
    form = Upform(data=request.POST, files=request.FILES)
    if form.is_valid():
        print(form.cleaned_data)
        # 读取到内容，自己处理每个字段的数据
        image_object = form.cleaned_data.get("img")

        # db_file_path = os.path.join("static", "img", image_object.name)
        # file_path = os.path.join("app02", db_file_path)
        # media_path = os.path.join(settings.MEDIA_ROOT, image_object.name)
        media_path = os.path.join("media", image_object.name)

        f = open(media_path, mode="wb")
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
        # 将图片文件路径写入到数据库
        Boss.objects.create(
            name=form.cleaned_data["name"],
            age=form.cleaned_data["age"],
            img=media_path
        )

        return HttpResponse("...")
    return render(request, "upload_form.html", {"form": form, "title": title})


class UpModelform(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]

    class Meta:
        model = City
        fields = "__all__"


def upload_modelform(request):
    title = "新建城市"
    if request.method == "GET":
        form = UpModelform()
        return render(request, "upload_form.html", {"form": form, "title": title})
    form = UpModelform(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件 : 自动保存
        form.save()
        return HttpResponse("上传成功")
    return render(request, "upload_form.html", {"form": form, "title": title})

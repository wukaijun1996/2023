from django.http import HttpResponse
from django.shortcuts import render,redirect
from app02.models import City
from app02.utils.bootstrap import BootStrapModelForm


def city_list(request):
    queryset = City.objects.all()

    return render(request, "city_list.html", {"queryset": queryset})


class UpModelform(BootStrapModelForm):
    bootstrap_exclude_fields = ["img"]

    class Meta:
        model = City
        fields = "__all__"


def city_add(request):

    title = "Modelform上传文件"
    if request.method == "GET":
        form = UpModelform()
        return render(request, "upload_form.html", {"form": form, "title": title})
    form = UpModelform(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件 : 自动保存
        form.save()
        return redirect("/city/list/")
    return render(request, "upload_form.html", {"form": form, "title": title})




from django.shortcuts import render, HttpResponse
from app02.models import Department, UserInfo


# Create your views here.

def depart_list(request):
    """部门列表"""

    queryset = Department.objects.all()
    print(queryset)

    return render(request, "depart_list.html", {"queryset": queryset})

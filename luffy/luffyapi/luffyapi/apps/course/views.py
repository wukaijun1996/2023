from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from course import models
from course import serializaer

from course.paginations import PageNumberPagination


class CourseCategoryView(GenericViewSet, ListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializaer.CourseCategorySerializaer


from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class CourseView(GenericViewSet, ListModelMixin):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializaer.CourseModelSerializaer
    # pagination_class = PageNumberPagination
    """
    drf自带过滤和排序，存在缺陷，对于关联字段不能过滤，故使用django-filter
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'price']  # 排序 /course/free/?ordering=price  , /course/free/?ordering=-id
    search_fields = ['id'] # 过滤 /course/free/?search=2
    """
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['id', 'price']
    filterset_fields = ['course_category']  # 过滤/course/free/?course_category=3

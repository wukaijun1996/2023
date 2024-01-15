from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from course import models
from course import serializaer

from course.paginations import PageNumberPagination


class CourseCategoryView(GenericViewSet, ListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializaer.CourseCategorySerializer


from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from course.filters import MyFilter, CourseFilterSet


class CourseView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """
    课程群查接口
    """
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializaer.CourseModelSerializer
    pagination_class = PageNumberPagination
    """
    drf自带过滤和排序，存在缺陷，对于关联字段不能过滤，故使用django-filter
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['id', 'price']  # 排序 /course/free/?ordering=price  , /course/free/?ordering=-id
    search_fields = ['id'] # 过滤 /course/free/?search=2
    """
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    # 参与搜索的字段
    search_fields = ['name', 'id', 'brief']  # 过滤 /course/free/?search=2
    # 允许排序的字段
    ordering_fields = ['id', 'price', 'students']
    #  过滤
    filterset_fields = ['course_category', 'id']  # 过滤/course/free/?course_category=3

    # django_filters 过滤用filterset_class 使用自定义类进行过滤，功能进行扩展，区间过滤
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = CourseFilterSet


class CourseChapterView(GenericViewSet, ListModelMixin):
    """
    课程章节接口
    """
    queryset = models.CourseChapter.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializaer.CourseChapterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course_id']


class CourseSearchView(GenericViewSet, ListModelMixin):
    """
    搜索接口
    """
    queryset = models.Course.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializaer.CourseModelSerializer
    pagination_class = PageNumberPagination

    filter_backends = [SearchFilter]
    # 参与搜索的字段
    search_fields = ['name']

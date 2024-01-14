from rest_framework.filters import BaseFilterBackend


class MyFilter(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        # 真正的过滤规则
        # params = request.query_params.get(self.ordering_param)
        # queryset.filter(***)
        return queryset[:2]


from django_filters.filterset import FilterSet
from django_filters import filters
from course import models


class CourseFilterSet(FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gt')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = models.Course
        fields = ['course_category']

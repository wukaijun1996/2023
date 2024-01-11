from rest_framework import serializers
from course import models


class CourseCategorySerializaer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class TeacherSerializaer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['name', 'title', 'role_name']


class CourseModelSerializaer(serializers.ModelSerializer):
    # 子序列化
    teacher = TeacherSerializaer()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'price', 'course_img', 'brief',
                  'teacher', 'course_type_name',
                  'status_name', 'level_name', 'section_list']

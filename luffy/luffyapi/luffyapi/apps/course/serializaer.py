from rest_framework import serializers
from course import models


class CourseCategorySerializaer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class TeacherSerializaer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'name', 'role_name', 'title', 'signature', 'image', 'brief']


class CourseModelSerializaer(serializers.ModelSerializer):
    # 子序列化
    teacher = TeacherSerializaer()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'course_img', 'brief',
                  'attachment_path', 'pub_sections', 'price',
                  'students', 'period', 'sections',
                  'course_type_name', 'level_name', 'status_name',
                  'teacher', 'section_list']

from rest_framework import serializers
from course import models


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'name', 'role_name', 'title', 'signature', 'image', 'brief']


class CourseModelSerializer(serializers.ModelSerializer):
    # 子序列化
    teacher = TeacherSerializer()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'course_img', 'brief',
                  'attachment_path', 'pub_sections', 'price',
                  'students', 'period', 'sections',
                  'course_type_name', 'level_name', 'status_name',
                  'teacher', 'section_list']


class CourseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseSection
        fields = ['name', 'orders', 'section_link', 'duration', 'free_trail']


class CourseChapterSerializer(serializers.ModelSerializer):
    coursesections = CourseSectionSerializer(many=True)

    class Meta:
        model = models.CourseChapter
        fields = ['id', 'name', 'chapter', 'summary', 'coursesections']

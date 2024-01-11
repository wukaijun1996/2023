from django.urls import path, re_path, include

from rest_framework.routers import SimpleRouter
from course import views

router = SimpleRouter()
router.register('categories', views.CourseCategoryView, 'categories')
router.register('free', views.CourseView, 'free')


urlpatterns = [
    path('', include(router.urls)),

]

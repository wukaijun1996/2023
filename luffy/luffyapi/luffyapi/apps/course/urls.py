from django.urls import path, re_path, include

from rest_framework.routers import SimpleRouter
from course import views

router = SimpleRouter()
router.register('categories', views.CourseCategoryView, 'categories')
router.register('actual', views.CourseView, 'actual')
router.register('chapters', views.CourseChapterView, 'chapters')
router.register('search', views.CourseSearchView, 'search')


urlpatterns = [
    path('', include(router.urls)),

]

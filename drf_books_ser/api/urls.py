from django.urls import path, re_path
from api import views

urlpatterns = [
    path('books/', views.BookAPIView.as_view()),
    re_path(r'books/(?P<pk>\d+)', views.BookAPIView.as_view()),
]

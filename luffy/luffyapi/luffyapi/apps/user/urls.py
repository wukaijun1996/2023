from django.urls import path, re_path, include

from rest_framework.routers import SimpleRouter
from user import views

router = SimpleRouter()
router.register('', views.LoginView, 'login')
router.register('', views.SendSmsView, 'send')
router.register('register', views.RegisterView, 'register')  # /user/register post就是新增

urlpatterns = [
    path('', include(router.urls)),

]

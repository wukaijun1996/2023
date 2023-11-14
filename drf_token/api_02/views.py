from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin

from api_02 import models
from api_02.ser import UserModelserializer


class RegisterView(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    queryset = models.User.objects.all()
    serializer_class = UserModelserializer

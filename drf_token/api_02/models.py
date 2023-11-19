from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=32, unique=True)
    icon = models.ImageField(upload_to='icon', default='icon/default.png')


class Book(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

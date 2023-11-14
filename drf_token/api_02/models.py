from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=32, unique=True)
    icon = models.ImageField(upload_to='icon', default='icon/default.png')

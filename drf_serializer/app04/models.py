from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_type = models.IntegerField(choices=((1, '超级用户'), (2, '普通用户'), (3, '二笔用户'),))

    def __str__(self):
        return self.username


class UserToken(models.Model):
    token = models.CharField(max_length=64)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)  # 一对一关联到User表

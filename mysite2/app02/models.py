from django.db import models


# Create your models here.

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=32)


class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额(总个数10位，小数点后2位)", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    """
    # 有约束
     -to 与哪张表关联
     -to_field,表中的哪一列关联 
     Django 自动 
      -写的depart
      -生成数据列depart_id
      部门表被删除时
    1.级联删除
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)
    2.置空
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.SET_NULL)
    """
    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)


    # 在Django 中做约束
    gender_choice = (
        (1, '男'),
        (1, '女'),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choice)

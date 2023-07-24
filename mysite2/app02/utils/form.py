from app02.models import Department, UserInfo, PrettyNum
from app02.utils.bootstrap import BootStrapModelForm
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class PrettyModelForm(BootStrapModelForm):
    # 校验手机号格式，必须按下面格式提交，不然不能提交
    mobile = forms.CharField(
        label="手机号码",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]
    )

    class Meta:
        model = PrettyNum
        # fields = ["mobile", "price", "level", "status"]
        # 要显示全部字段是也可以直接 add  "__all__"
        # 如果是除XX字段
        # exclude = ["level"]
        fields = "__all__"

    # 钩子方法 校验手机号格式，必须按下面要求提交，不然不能提交
    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        print(self.instance.pk, "嘿嘿")
        # 获取用户传入的数据
        input_mobile = self.cleaned_data["mobile"]
        # 判断用户输入的手机号在数据库中是否已存在
        if PrettyNum.objects.filter(mobile=input_mobile).exists():
            raise ValidationError("手机号已存在1")
        if len(input_mobile) != 11:
            raise ValidationError("格式错误")
        return input_mobile


class UserModelForm(BootStrapModelForm):
    # 校验规则重写数据库的字段属性
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "age": forms.TextInput(attrs={"class": "form-control"}),
        # }
        # 上述方法麻烦，重写初始化方法(为了给输入框加样式)


class PrettyEditModelForm(BootStrapModelForm):
    # mobile = forms.CharField(disabled=True)

    class Meta:
        model = PrettyNum
        fields = ["mobile", "price", "level", "status"]

    # 钩子方法 校验手机号格式，必须按下面要求提交，不然不能提交
    def clean_mobile(self):
        # 当前编辑的哪一行的ID
        print(self.instance.pk)
        # 获取用户传入的数据
        input_mobile = self.cleaned_data["mobile"]
        # 当编辑模式下校验号码是否存在 （exclude(id=self.instance.pk) 过滤掉自己）
        exists = PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=input_mobile).exists()
        print(exists)
        if exists:
            raise ValidationError("手机号已存在")
        if len(input_mobile) != 11:
            raise ValidationError("格式错误")
        return input_mobile

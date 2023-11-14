from rest_framework import serializers
from api_02 import models
from rest_framework.exceptions import ValidationError


class UserModelserializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=16, min_length=4, required=True, write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'mobile', 're_password', 'icon']
        extra_kwargs = {
            'username': {'max_length': 16},
            'password': {'write_only': True}
        }

    # 局部钩子
    def validate_mobile(self, data):
        if not len(data) == 11:
            raise ValidationError("手机号不合法")
        return data

    # 全局钩子
    def validate(self, attrs):
        if not attrs.get('password') == attrs.get('re_password'):
            raise ValidationError('两次密码不一致')
        attrs.pop('re_password')
        return attrs

    def create(self, validated_data):
        # models.User.objects.create(**validated_data) 这个密码不会加密
        user = models.User.objects.create_user(**validated_data)  # 这个会加密
        return user

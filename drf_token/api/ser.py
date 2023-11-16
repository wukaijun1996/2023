from rest_framework import serializers
from api_02 import models
import re
from rest_framework.exceptions import ValidationError

from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler


class LoginModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    ps = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['name', 'ps']

    def validate(self, attrs):
        print('giao', self.context.get('request').method)
        username = attrs.get('name')
        print(username)
        password = attrs.get('ps')
        print(password)
        if re.match('^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(mobile=username).first()
        elif re.match('^.+@.+$', username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()

        if user:  # 存在用户
            # 校验密码是密文， 要用check_password
            if user.check_password(password):
                # 需要签发token
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                self.context['token'] = token
                self.context['username'] = user.username
                return attrs
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

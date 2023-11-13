from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework_jwt.authentication import get_authorization_header, jwt_get_username_from_payload, \
    JSONWebTokenAuthentication
from rest_framework import exceptions
import jwt
from django.utils.translation import ugettext as _


class MyToken(JSONWebTokenAuthentication):
    def authenticate(self, request):
        jwt_value = str(request.META.get('HTTP_AUTHORIZATION'))
        # 认证
        try:
            payload = jwt_decode_handler(jwt_value)
            user = self.authenticate_credentials(payload)
            print(user.username, "giao")
        except Exception:
            raise exceptions.AuthenticationFailed('认证失败')

        return payload, None

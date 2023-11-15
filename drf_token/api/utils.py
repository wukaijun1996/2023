
# 自定义控制jwt 登录接口的返回数据格式
def my_jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'msg': '登录成功',
        'status': 100,
        'username': user.username
    }

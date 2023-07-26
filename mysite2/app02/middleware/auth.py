from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    """中间件1"""

    def process_request(self, request):

        # 排除那些不需要登录就能访问的页面
        #  request.path_info 获取当前用户请求的URL
        if request.path_info in ["/login/", "/image/code/"]:
            return
        # 1.读取当前访问的用户的session信息，如果能读到，说明已登录过，就可以继续向后走
        info_list = request.session.get("info")
        if info_list:
            return
        # 没有登录过，重新回到登录页面
        return redirect("/login/")

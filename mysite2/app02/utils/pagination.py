"""
自定义的分页组件，以后如果想要使用这个分页组件， just do the following

在视图函数中
def pretty_list(request):

    # 根据自己的情况筛选自鹅蛋的数据
    queryset = PrettyNum.objects.all()
    # 实例化分页对象
    page_object = Pagination(request, queryset)
    # 分页完的数据
    page_queryset = page_object.page_queryset
    # 生成的页码html
    page_string = page_object.html()

    context = {
        "queryset": page_queryset,# 分完页的数据
        "page_string": page_string  # 页码
    }
    return render(request, "pretty_list.html", context)

在html页面中
        {% for obj in queryset %}
        {{obj.xxx}}
        {% endfor %}

        <div class="clearfix">
        <ul class="pagination" style="float: left">
            {{ page_string }}
            <li>
                <form action="" method="get" style="float: left; margin-left: -1px">
                    <div class="input-group" style="width: 150px">
                        <input style="border-radius: 0" type="text" name="page" class="form-control" placeholder="页码">
                        <span class="input-group-btn">
                            <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                        </span>
                    </div>
                </form>
            </li>
        </ul>
            </div>

"""
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        """
        :param request: 请求的对象
        :param queryset:  符合条件的数据
        :param page_size: 每页显示多少条数据
        :param page_param: 在url中传递的获取分页的参数。 age : /pretty/list/?page=12
        :param plus: 显示当前页的 前或后几页（页码）
        """
        page = request.GET.get(page_param, "1")  # mean 当前页码
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start:self.end]

        # 增加页码功能页码
        # 数据总条数
        self.total_count = queryset.count()
        # print(total_count)
        # 总页码
        total_page_count, div = divmod(self.total_count, self.page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 计算出，显示当前页的前5页，后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库中的数据比较少，都没有达到11页
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中的数据比较多 > 11页
            # 当前页<5时
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页>5时
                # 当前页 + 5 > 总页面
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        # 页码
        page_str_list = []
        # 首页
        page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))

        # 上一页
        if self.page == 1:
            prev = '<li><a href="?page={}">上一页</a></li>'.format(self.page)
            page_str_list.append(prev)
        else:
            prev = '<li><a href="?page={}">上一页</a></li>'.format(self.page - 1)
            page_str_list.append(prev)

        for i in range(start_page, end_page + 1):
            if i == self.page:
                ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
                page_str_list.append(ele)
                continue
            ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
            page_str_list.append(ele)
        # 下一页
        if self.page == self.total_page_count:
            prev = '<li><a href="?page={}">下一页</a></li>'.format(self.page)
            page_str_list.append(prev)
        else:
            prev = '<li><a href="?page={}">下一页</a></li>'.format(self.page + 1)
            page_str_list.append(prev)

        # 尾页
        page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(self.total_page_count))

        page_string = mark_safe("".join(page_str_list))

        return page_string

from django.db import models


# Create your models here.
class BaseModel(models.Model):
    is_delete = models.BooleanField(choices=((0, '未删除'), (1, '删除')), default=0)
    # auto_now_add=True 只要记录创建，不需要手动插入时间，自动把当前时间插入
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now 只要更新 就会把当前时间插入
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        # 单个字段 有索引 有唯一
        # 多个字段 有联合索引 联合唯一
        abstract = True  # 抽象表 不在数据库中建表


class Book(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='书名')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 一对多的关系一旦确立 关联字段写在多的一方
    # to_field 默认不写 关联到Publish主键
    # db_constraint=False 逻辑上的关联 实际上没有外键联系 增删不会受外键影响  orm查询不影响
    publish = models.ForeignKey(to='Publish', on_delete=models.DO_NOTHING, db_constraint=False)

    # 多对多 跟作者 关联字段写在查询次多的一方

    # 什么时候用自动 什么时候用手动？ 第三张表只有关联字段 用自动， 第三张表有扩展字段 需要手动
    authors = models.ManyToManyField(to='Author', db_constraint=False)

    class Meta:
        verbose_name_plural = '书表'  # admin中书名的显示

    def __str__(self):
        return self.name

    @property
    def publish_name(self):
        return self.publish.name

    @property
    def author_list(self):
        author_list = self.authors.all()
        # ll = []
        # for author in author_list:
        #     ll.append({'name': author.name, 'sex': author.get_sex_display()})
        # return ll
        return [{'name': author.name, 'sex': author.get_sex_display()} for author in author_list]


class Publish(BaseModel):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=32)
    sex = models.IntegerField(choices=((1, '男'), (2, '女')))
    # 一对一 关系 写在查询频率高的一方
    authordetail = models.OneToOneField(to='AuthorDetail', db_constraint=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AuthorDetail(BaseModel):
    mobile = models.CharField(max_length=11)

    def __str__(self):
        return self.mobile

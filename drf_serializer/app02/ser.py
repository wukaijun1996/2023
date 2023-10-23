from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from app01.models import Book


class BookSerializer(serializers.Serializer):
    title1 = serializers.CharField(source="title")
    price = serializers.CharField()
    pub_date = serializers.CharField()
    publish1 = serializers.CharField(source="publish.email")  # 相当于book.publish.email
    # authors = serializers.CharField(source="authors.all")
    authors = serializers.SerializerMethodField()  # 需要有个配套方法 方法名叫 get_字段名, 返回值就是要显示的东西

    def get_authors(self, instance):
        # instance 是 book对象
        authors = instance.authors.all()  # 取出所有作者
        ll = []
        print(authors)
        for author in authors:
            ll.append({'name': author.name, 'age': author.age})
        return ll

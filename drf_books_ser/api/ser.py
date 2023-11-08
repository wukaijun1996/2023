from rest_framework import serializers

from api import models


# 写一个类 继承ListSerializer 重写update
class BookListSerializer(serializers.ListSerializer):
    # def create(self, validated_data):
    #     print(validated_data)
    #     super(BookListSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        print(instance)
        print(validated_data)
        print(type(self.child))  # api.ser.BookModelSerializer
        # 保存数据
        return [
            self.child.update(instance[i], attrs) for i, attrs in enumerate(validated_data)
        ]


# 如果系列化的是数据库的表 尽量用ModelSerializer
class BookModelSerializer(serializers.ModelSerializer):
    # 第一种方案 只序列化可以 反序列化有问题
    # publish = serializers.CharField(source='publish.name')

    # 第一种方案 只序列化可以 反序列化有问题
    class Meta:
        list_serializer_class = BookListSerializer
        model = models.Book
        # fields = '__all__'
        fields = ('name', 'price', 'authors', 'author_list', 'publish', 'publish_name')
        # depth = 1  # 用的少 显示连表层级
        extra_kwargs = {
            'publish': {'write_only': True},
            'publish_name': {'read_only': True},
            'authors': {'write_only': True},
            'author_list': {'read_only': True},
        }

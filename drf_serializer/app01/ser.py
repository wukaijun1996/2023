from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def check_author(data):
    if data.startswith("sb"):
        raise ValidationError("作者名字不能以sb开头")


class BookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=16, min_length=4, required=True, error_messages={"required": "是的"})
    price = serializers.CharField(write_only=True, required=True)
    author = serializers.CharField(validators=[check_author])  # validators=[] 列表中写函数内存地址
    publish = serializers.CharField()

    def validate_price(self, data):  # validate_字段名 接收一个参数 （局部钩子）
        # 如果价格小于10 就校验不通过
        # print(type(data))
        # print(data)
        # return data
        if float(data) > 10:
            return data
        else:
            raise ValidationError("价格太低")

    def validate(self, validate_data):
        print(validate_data)
        author = validate_data.get("author")
        publish = validate_data.get("publish")
        if author == publish:
            raise ValidationError("作者名字跟出版社一样")
        return validate_data

    def update(self, instance, validated_data):
        # instance是book这个对象
        # validated_data是校验后的数据
        instance.name = validated_data.get('name')
        instance.price = validated_data.get('price')
        instance.author = validated_data.get('author')
        instance.publish = validated_data.get('publish')
        instance.save()
        return instance

from rest_framework.serializers import ModelSerializer
from app01.models import Book


# 新建序列化类
class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

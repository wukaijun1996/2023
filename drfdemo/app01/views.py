from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app01.models import Book
from app01.ser import BookModelSerializer


# Create your views here.
class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

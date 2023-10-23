from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from app02.models import Book
from app02.ser import BookSerializer
from rest_framework.response import Response


class APP02BookView(APIView):
    def get(self, request, pk):
        book = Book.objects.filter(id=pk).first()
        book_ser = BookSerializer(instance=book)
        return Response(book_ser.data)

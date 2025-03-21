from django.shortcuts import render
from .serializers import BookListSerializer,BookSerializer
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookListSerializer(books,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk = book_pk)
    serializer = BookSerializer(book)
    return Response(serializer.data)
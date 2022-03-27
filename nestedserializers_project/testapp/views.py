from django.shortcuts import render
from testapp.models import Author, Book
from testapp.serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

class AuthorListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

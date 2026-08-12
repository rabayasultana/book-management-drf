from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import generics

from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthenticatedOrReadOnly


class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]

    filterset_fields = [
        'category',
        'author'
    ]

    search_fields = [
        'title',
        'author'
    ]

    ordering_fields = [
        'title',
        'price',
        'published_date'
    ]

    ordering = ['id']


class BookDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]


def book_list(request):
    return render(
        request,
        'books/book_list.html'
    )


@login_required
def book_create(request):
    return render(
        request,
        'books/book_form.html'
    )
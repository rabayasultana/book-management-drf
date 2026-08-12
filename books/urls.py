from django.urls import path

from .views import (
    BookListCreateView,
    BookDetailView,
    book_list,
    book_create,
)


urlpatterns = [

    # UI
    path(
        '',
        book_list,
        name='book_list'
    ),
    path(
        'book/add/',
        book_create,
        name='book_create'
    ),

    # REST API
    path(
        'books/',
        BookListCreateView.as_view(),
        name='book-list-create'
    ),

    path(
        'books/<int:pk>/',
        BookDetailView.as_view(),
        name='book-detail'
    ),
]
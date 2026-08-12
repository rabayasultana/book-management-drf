from django.urls import path

from .views import (
    BookListCreateView,
    BookDetailView,
    book_list,
    book_create,
    book_detail,
    book_edit,
    book_delete,
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
     path(
        'book/<int:pk>/',
        book_detail,
        name='book_detail'
    ),
     path(
        'book/<int:pk>/edit/',
        book_edit,
        name='book_edit'
    ),

    path(
        'book/<int:pk>/delete/',
        book_delete,
        name='book_delete'
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
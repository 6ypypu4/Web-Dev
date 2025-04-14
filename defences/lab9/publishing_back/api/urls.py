from django.urls import path
from .views import (
    PublisherList, PublisherDetail, PublisherBooksList,
    BookList, BookDetail, TopTenBooks
)

urlpatterns = [
    path('publishers/', PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
    path('publishers/<int:pk>/books/', PublisherBooksList.as_view(), name='publisher-books'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/top_ten/', TopTenBooks.as_view(), name='top-ten-books'),
]
from rest_framework import generics
from .models import Publisher, Book
from .serializers import PublisherSerializer, BookSerializer

class PublisherList(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetail(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherBooksList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Publisher.objects.all()


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class TopTenBooks(generics.ListAPIView):
    queryset = Book.objects.order_by('-price')[:10]
    serializer_class = BookSerializer
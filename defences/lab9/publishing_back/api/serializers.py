from rest_framework import serializers
from .models import Book, Publisher

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'synopsis', 'price', 'publisher']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id',  'name', 'description', 'city', 'address', 'books']

from rest_framework import serializers
from library.models import Book, Author, Alt


class BookSerializer(serializers.ModelSerializer):
    # alt_set = AltSerializer(book.alt_set.all(), many=True)

    class Meta:
        model = Book
        fields = ['id', 'title']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'books']


class AltSerializer(serializers.ModelSerializer):
    # books = BookSerializer

    class Meta:
        model = Alt
        fields = ['id', 'title', 'book']

from rest_framework import serializers
from library.models import Book, Author, Alt


class AuthorSerializer:
    pass


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors']


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'book_list']


class AltSerializer(serializers.ModelSerializer):
    # book = BookSerializer(source='book')
    book = serializers.RelatedField(source='book', read_only=True)

    class Meta:
        model = Alt
        fields = ['id', 'title', 'book']

from rest_framework import serializers
from library.models import Book, Author, Alt


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Book
        fields = ['id', 'title', 'authors']


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'book_list']


class AltSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Alt
        fields = ['id', 'title', 'book']

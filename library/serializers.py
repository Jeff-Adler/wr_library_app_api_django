from rest_framework import serializers
from library.models import Book, Author, Alt


class BookSerializer(serializers.ModelSerializer):
    # authors = AuthorSerializer(book.author_set.all(), many=True)
    # alts = AltSerializer(book.alt_set.all(), many=True)
    alts = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'alts']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'books']


class AltSerializer(serializers.ModelSerializer):
    # book = BookSerializer(source='book')
    book = serializers.RelatedField(source='book', read_only=True)

    class Meta:
        model = Alt
        fields = ['id', 'title', 'book']

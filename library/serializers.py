from rest_framework import serializers
from library.models import Book, Author, Alt


class BookSerializer(serializers.ModelSerializer):
    # author_list = AuthorSerializer(ead_only=True, many=True)
    authors = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), many=True)
    # alts = AltSerializer(book.alt_set.all(), many=True)
    # alts = serializers.RelatedField(many=True, read_only=True)

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

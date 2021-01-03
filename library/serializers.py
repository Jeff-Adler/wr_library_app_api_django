from rest_framework import serializers
from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(
    #     required=False, allow_blank=True, max_length=100)

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Book` instance, given the validated data.
    #     """
    #     return Book.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Book` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.save()
    #     return instance

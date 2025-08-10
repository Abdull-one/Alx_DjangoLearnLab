from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes the Book model, ensuring publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation: Ensure publication year is not greater than the current year.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model, including nested books.
    Uses the BookSerializer for the related books field.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer (reverse relation)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

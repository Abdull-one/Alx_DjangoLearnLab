from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
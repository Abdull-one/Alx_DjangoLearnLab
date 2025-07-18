import os
print("Current working directory:", os.getcwd())
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))

import os
import django
import sys
import os
import django

# Make sure Django can find the project settings
sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian

# Sample Queries

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return []

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

# Example usage
if __name__ == '__main__':
    print("Books by Author 'John Doe':")
    for book in books_by_author('John Doe'):
        print(f"- {book.title}")

    print("\nBooks in Library 'Central Library':")
    for book in books_in_library('Central Library'):
        print(f"- {book.title}")

    print("\nLibrarian of 'Central Library':")
    librarian = get_librarian('Central Library')
    if librarian:
        print(f"- {librarian.name}")
    else:
        print("No librarian assigned.")

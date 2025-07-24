from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
orwell = Author.objects.get(name="George Orwell")
books_by_orwell = Book.objects.filter(author=orwell)

# List all books in a library
central_library = Library.objects.get(name="Central Library")
books_in_central = central_library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=central_library)

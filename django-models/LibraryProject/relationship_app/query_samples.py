from .models import Author, Book, Librarian

# Query all books by a specific author
author_books = Book.objects.filter(author__name="Author Name")

# List all books in a library
library_books = Book.objects.filter(library__name="Library Name")

# Get the librarian of a specific library
librarian = Librarian.objects.filter(library__name="Library Name").first()
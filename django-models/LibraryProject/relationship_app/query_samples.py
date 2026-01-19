from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_books = Book.objects.filter(author__name="Author Name")

# List all books in a library
library = Library.objects.get(name="Central Library")
books = library.books.all()

# Get the librarian of a specific library
librarian = Librarian.objects.get(library__name="Library Name")
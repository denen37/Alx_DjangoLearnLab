### Creating a Book Instance

```python
    from bookshelf.models import Book
    book1 = Book(title="1984", author="George Orwell", publication_year=1949)
    book1.save()

    //If it does not throw an error, the book was created successfully.
```


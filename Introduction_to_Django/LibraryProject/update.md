### Updating a book instance

```python
    from bookshelf.models import Book

    book = Book.objects.get(id=1)
    book.title = "Nineteen Eigthy-Four"
    book.save()

    //If it does not throw an error, then the update was successful.
    //To view the updated book, retrieve it from the database and print it.
```

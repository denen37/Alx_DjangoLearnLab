### Retrieving all books

```python
    from bookshelf.models import Book
    books = Book.objects.all()
    for book in books:
        print(book)
 
    //Output:
    //1984 by George Orwell (1949)

    //Note: To produce the above output, we have to define the __str__ method in the Book model.
```
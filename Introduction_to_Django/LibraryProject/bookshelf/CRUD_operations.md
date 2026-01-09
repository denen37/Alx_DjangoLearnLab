### Creating a Book Instance

```python
    from bookshelf.models import Book

    book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
    print(book1)
 
    //Output:
    //1: 1984 by George Orwell (1949)
```

### Retrieving a book instance

```python
    from bookshelf.models import Book

    book = Book.objects.get(id=1)
    print(book)
 
    //Output:
    //1: 1984 by George Orwell (1949)

    //Note: To produce the above output, we have to define the __str__ method in the Book model.
```

### Updating a book instance

```python
    from bookshelf.models import Book

    book = Book.objects.get(id=1)
    book.title = "Nineteen Eigthy-Four"
    book.save()

    //If it does not throw an error, then the update was successful.
    //To view the updated book, retrieve it from the database and print it.
```


### Deleting a book instance

```python
    from bookshelf.models import Book

    book = Book.objects.get(id=1)
    num = book.delete()
    print(num)

    //Output:
    //(1, {'bookshelf.Book': 1})
```
### Retrieving a book instance

```python
        from bookshelf.models import Book

        book = Book.objects.get(id=1)
        print(book)
    
        //Output:
        //1: 1984 by George Orwell (1949)


    //Note: To produce the above output, we have to define the __str__ method in the Book model.
```
### Deleting a book instance

```python
    from bookshelf.models import Book

    book = Book.objects.get(id=1)
    num = book.delete()
    print(num)

    //Output:
    //(1, {'bookshelf.Book': 1})
```
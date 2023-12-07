# test_Book.py
from Book import Book

def test_book_creation():
    book = Book("Title", "Author", 5)
    assert book.title == "Title"
    assert book.author == "Author"
    assert book.quantity == 5
    assert book.available is True

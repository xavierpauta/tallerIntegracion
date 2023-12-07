# test_Library.py
from Library import Library
from Book import Book


def test_add_book_to_library():
    library = Library()
    book = Book("Title", "Author", 5)
    library.add_book(book)
    assert book in library.catalog


def test_display_catalog():
    library = Library()
    book1 = Book("Title1", "Author1", 3)
    book2 = Book("Title2", "Author2", 7)
    library.add_book(book1)
    library.add_book(book2)

    expected_output = "Title1 by Author1 - Disponible\nTitle2 by Author2 - Disponible\n"
    assert library.display_catalog() == expected_output

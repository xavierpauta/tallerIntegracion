# test_All.py


from src.main.Book import Book
from src.main.Library import Library
from src.main.Verificador import CheckoutSystem
from src.main.User import User

from datetime import datetime, timedelta


def test_book_creation():
    book = Book("Title", "Author", 5)
    assert book.title == "Title"
    assert book.author == "Author"
    assert book.quantity == 5
    assert book.available is True


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


def test_validate_quantity():
    assert CheckoutSystem.validate_quantity(5) == 5
    assert CheckoutSystem.validate_quantity(0) == -1
    assert CheckoutSystem.validate_quantity("invalid") == -1

def test_calculate_due_date():
    today = datetime.now()
    due_date = CheckoutSystem.calculate_due_date()
    expected_due_date = today + timedelta(days=14)
    assert due_date.date() == expected_due_date.date()

def test_calculate_late_fee():
    today = datetime.now()
    due_date = today - timedelta(days=7)
    assert CheckoutSystem.calculate_late_fee(due_date) == 7
    assert CheckoutSystem.calculate_late_fee(today) == 0

def test_checkout():
    user = User()
    library = [Book("Title1", "Author1", 5), Book("Title2", "Author2", 3)]
    user.select_book(library[0], 2)
    user.select_book(library[1], 1)
    CheckoutSystem.checkout(user)

    assert library[0].quantity == 3
    assert library[1].quantity == 2

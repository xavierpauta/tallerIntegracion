# test_CheckoutSystem.py
from datetime import datetime, timedelta
from Verificador import CheckoutSystem
from User import User
from Book import Book

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

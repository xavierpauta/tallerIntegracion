# Book.py
class Book:
    def __init__(self, title, author, quantity, available=True):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available = available

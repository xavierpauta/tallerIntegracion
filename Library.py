# Library.py
from Book import Book

class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def display_catalog(self):
        for book in self.catalog:
            status = "Disponible" if book.available else "No Disponible"
            print(f"{book.title} por {book.author} - {status}")

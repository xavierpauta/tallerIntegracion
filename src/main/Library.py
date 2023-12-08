# Library.py

from src.main.Book import Book

class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)

    def display_catalog(self):
        catalog_output = ""
        for book in self.catalog:
            status = "Disponible" if book.available else "No Disponible"
            catalog_output += f"{book.title} by {book.author} - {status}\n"
        return catalog_output

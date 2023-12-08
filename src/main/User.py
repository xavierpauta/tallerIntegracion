# User.py
class User:
    def __init__(self):
        self.selected_books = []

    def select_book(self, book, quantity):
        self.selected_books.append({'book': book, 'quantity': quantity})

    def display_selection(self):
        for selection in self.selected_books:
            print(f"{selection['quantity']} x {selection['book'].title}")

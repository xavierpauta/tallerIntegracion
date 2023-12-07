


# main.py
from Book import Book
from Library import Library
from User import User
from Verificador import CheckoutSystem

def main():
    # Crear libros
    book1 = Book("El Gran Gatsby", "F. Scott Fitzgerald", 5)
    book2 = Book("Matar a un Ruiseñor", "Harper Lee", 3)
    book3 = Book("1984", "George Orwell", 8)

    # Crear la biblioteca y agregar libros
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Crear usuario
    user = User()

    # Mostrar catálogo
    print("Catálogo de libros:")
    library.display_catalog()

    # Seleccionar libros para el préstamo
    while True:
        title = input("Ingrese el título del libro que desea tomar prestado (o 'fin' para salir): ")
        if title.lower() == 'fin':
            break

        book = next((b for b in library.catalog if b.title.lower() == title.lower()), None)
        if book:
            quantity = int(input(f"Ingrese la cantidad de '{book.title}' que desea tomar prestada: "))
            quantity = CheckoutSystem.validate_quantity(quantity)

            if quantity != -1:
                user.select_book(book, quantity)
                print(f"Se seleccionaron {quantity} copias de '{book.title}' para préstamo.\n")
        else:
            print(f"Error: '{title}' no encontrado en el catálogo.\n")

    # Mostrar selección del usuario
    print("\nSelección del usuario:")
    user.display_selection()

    # Realizar el proceso de préstamo
    checkout_confirmation = input("¿Desea confirmar el préstamo? (s/n): ")
    if checkout_confirmation.lower() == 's':
        CheckoutSystem.checkout(user)
    else:
        print("Proceso de préstamo cancelado.")

    # Proceso de devolución
    return_confirmation = input("\n¿Desea procesar la devolución de libros? (s/n): ")
    if return_confirmation.lower() == 's':
        # Asumimos que el usuario devuelve exactamente lo que tomó prestado
        CheckoutSystem.return_books(user)

if __name__ == "__main__":
    main()

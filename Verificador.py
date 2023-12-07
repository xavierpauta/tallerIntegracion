# CheckoutSystem.py
from datetime import datetime, timedelta
from User import User

class CheckoutSystem:
    @staticmethod
    def validate_quantity(quantity):
        try:
            quantity = int(quantity)
            if quantity > 0:
                return quantity
            else:
                print("Error: La cantidad debe ser un número entero positivo.")
                return -1
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido para la cantidad.")
            return -1

    @staticmethod
    def calculate_due_date():
        return datetime.now() + timedelta(days=14)

    @staticmethod
    def calculate_late_fee(due_date):
        today = datetime.now()
        if today > due_date:
            days_late = (today - due_date).days
            return days_late * 1
        return 0

    @staticmethod
    def checkout(user):
        for selection in user.selected_books:
            book = selection['book']
            quantity = selection['quantity']

            if not book.available:
                print(f"Error: {book.title} no está disponible.")
                return -1

            if quantity > book.quantity:
                print(f"Error: No hay suficientes copias de {book.title} disponibles.")
                return -1

            book.quantity -= quantity
            book.available = book.quantity > 0

            due_date = CheckoutSystem.calculate_due_date()
            late_fee = CheckoutSystem.calculate_late_fee(due_date)

            print(f"¡Éxito al realizar el préstamo!\n"
                  f"{quantity} x {book.title} por {book.author}\n"
                  f"Fecha de devolución: {due_date}\n"
                  f"Multa por demora: ${late_fee}")

    @staticmethod
    def return_books(user):
        total_late_fee = 0
        for selection in user.selected_books:
            book = selection['book']
            quantity = selection['quantity']

            due_date = CheckoutSystem.calculate_due_date()
            late_fee = CheckoutSystem.calculate_late_fee(due_date)

            total_late_fee += late_fee

            book.quantity += quantity
            book.available = True

        print(f"¡Devolución exitosa!\n"
              f"Multa total por demora: ${total_late_fee}")

def main():
    # Implementa la lógica del programa principal aquí
    pass

if __name__ == "__main__":
    main()

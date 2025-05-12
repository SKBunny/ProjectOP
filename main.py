# Головний модуль програми для управління барбершопом з консольним інтерфейсом
from datetime import datetime, timedelta
from barbershop import BarberShop
# Імпортуємо всі функції з модуля Service
from Service import (print_menu, print_customer_menu, print_barber_menu, print_appointment_menu,
                    print_schedule_menu, print_service_menu, handle_customer_menu, handle_barber_menu,
                    handle_appointment_menu, handle_schedule_menu, handle_service_menu, parse_date, format_date,
                    clear_screen)

def main():
    # Головна функція програми
    barbershop = BarberShop("Frisor")

    print(f"Ласкаво просимо до {barbershop.name}!")

    while True:
        print_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            handle_customer_menu(barbershop)
        elif choice == "2":
            handle_barber_menu(barbershop)
        elif choice == "3":
            handle_service_menu(barbershop)
        elif choice == "4":
            handle_appointment_menu(barbershop)
        elif choice == "5":
            handle_schedule_menu(barbershop)
        elif choice == "0":
            print("Дякуємо за використання системи управління барбершопом!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
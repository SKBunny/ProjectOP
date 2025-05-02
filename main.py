# Головний модуль програми для управління барбершопом з консольним інтерфейсом
from datetime import datetime, timedelta
from barbershop import BarberShop

def clear_screen():
    # Очищає екран консолі
    print("\n" * 50)

def format_date(date_obj):
    # Форматує об'єкт дати у рядок
    return date_obj.strftime("%d-%m-%Y %H:%M")

def parse_date(date_str, format_str="%d-%m-%Y"):
    # Перетворює рядок дати в об'єкт datetime
    try:
        return datetime.strptime(date_str, format_str)
    except ValueError:
        print(f"Помилка: Некоректний формат дати. Використовуйте {format_str}")
        return None


def print_menu():
    # Виводить головне меню програми
    print("\n=== МЕНЮ БАРБЕРШОПУ ===")
    print("1. Управління клієнтами")
    print("2. Управління фахівцями")
    print("3. Управління записами")
    print("4. Перегляд розкладу")
    print("0. Вихід")
    print("======================")

def print_customer_menu():
    # Виводить меню управління клієнтами
    print("\n=== УПРАВЛІННЯ КЛІЄНТАМИ ===")
    print("1. Додати нового клієнта")
    print("2. Переглянути всіх клієнтів")
    print("3. Знайти клієнта за номером телефону")
    print("4. Переглянути всі записи клієнта")
    print("0. Повернутися до головного меню")
    print("=============================")

def print_barber_menu():
    # Виводить меню управління фахівцями
    print("\n=== УПРАВЛІННЯ ФАХІВЦЯМИ ===")
    print("1. Додати нового фахівця")
    print("2. Переглянути всіх фахівців")
    print("3. Встановити робочі години для фахівця")
    print("4. Переглянути розклад фахівця")
    print("0. Повернутися до головного меню")
    print("=============================")

def print_appointment_menu():
    # Виводить меню управління записами
    print("\n=== УПРАВЛІННЯ ЗАПИСАМИ ===")
    print("1. Створити новий запис")
    print("2. Скасувати запис")
    print("3. Позначити запис як виконаний")
    print("4. Переглянути всі записи на певну дату")
    print("0. Повернутися до головного меню")
    print("=============================")

def print_schedule_menu():
    # Виводить меню перегляду розкладу
    print("\n=== ПЕРЕГЛЯД РОЗКЛАДУ ===")
    print("1. Переглянути доступних фахівців на певну дату")
    print("2. Переглянути доступні слоти для фахівця на певну дату")
    print("0. Повернутися до головного меню")
    print("==========================")

def handle_customer_menu(barbershop):
    # Обробляє меню управління клієнтами
    while True:
        print_customer_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я клієнта: ")
            phone = input("Введіть номер телефону клієнта: ")
            email = input("Введіть електронну пошту клієнта (не обов'язково): ") or None

            customer = barbershop.add_customer(name, phone, email)
            if customer:
                print(f"Клієнта {name} успішно додано!")
            else:
                print("Не вдалося додати клієнта. Перевірте правильність введених даних.")

        elif choice == "2":
            if not barbershop.customers:
                print("Немає жодного клієнта.")
            else:
                print("\n=== СПИСОК КЛІЄНТІВ ===")
                for i, customer in enumerate(barbershop.customers, 1):
                    print(f"{i}. {customer.__repr__()}")

        elif choice == "3":
            phone = input("Введіть номер телефону для пошуку: ")
            customer = barbershop.find_customer_by_phone(phone)
            if customer:
                print(f"Знайдено клієнта: {customer.__repr__()}")
            else:
                print("Клієнта з таким номером телефону не знайдено.")

        elif choice == "4":
            phone = input("Введіть номер телефону клієнта: ")
            customer = barbershop.find_customer_by_phone(phone)
            if customer:
                appointments = customer.get_appointments()
                if not appointments:
                    print(f"У клієнта {customer.name} немає жодного запису.")
                else:
                    print(f"\n=== ЗАПИСИ КЛІЄНТА {customer.name} ===")
                    for i, appointment in enumerate(appointments, 1):
                        print(f"{i}. {appointment.__repr__()}")
            else:
                print("Клієнта з таким номером телефону не знайдено.")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")

        input("\nНатисніть Enter, щоб продовжити...")

def handle_schedule_menu(barbershop):
    # Обробляє меню перегляду розкладу
    while True:
        print_schedule_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            # Перегляд доступних фахівців на певну дату
            date_str = input("Введіть дату (ДД-ММ-РРРР): ")
            time_str = input("Введіть час (ГГ:ХХ): ")
            try:
                date = datetime.strptime(f"{date_str} {time_str}", "%d-%m-%Y %H:%M")
                available_barbers = barbershop.get_available_barbers(date)

                if not available_barbers:
                    print(f"На {date_str} о {time_str} немає доступних фахівців.")
                else:
                    print(f"\n=== ДОСТУПНІ ФАХІВЦІ НА {date_str} о {time_str} ===")
                    for i, barber in enumerate(available_barbers, 1):
                        print(f"{i}. {barber.__repr__()}")
            except ValueError:
                print("Помилка: Неправильний формат дати або часу.")

        elif choice == "2":
            # Перегляд доступних слотів для фахівця на певну дату
            if not barbershop.barbers:
                print("Немає жодного фахівця.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            print("\n=== СПИСОК ФАХІВЦІВ ===")
            for i, barber in enumerate(barbershop.barbers, 1):
                print(f"{i}. {barber.__repr__()}")

            try:
                barber_idx = int(input("Виберіть номер фахівця: ")) - 1
                barber = barbershop.barbers[barber_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            if not barbershop.services:
                print("Немає жодної послуги. Слоти будуть показані для стандартної тривалості 30 хв.")
                service = None
            else:
                print("\n=== СПИСОК ПОСЛУГ ===")
                for i, service in enumerate(barbershop.services, 1):
                    print(f"{i}. {service.__repr__()}")

                try:
                    service_idx = int(input("Виберіть номер послуги (або 0 для стандартної тривалості): ")) - 1
                    service = None if service_idx < 0 else barbershop.services[service_idx]
                except (ValueError, IndexError):
                    print("Неправильний ввід. Буде використана стандартна тривалість 30 хв.")
                    service = None

            date_str = input("Введіть дату (ДД-ММ-РРРР): ")
            date = parse_date(date_str)
            if not date:
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            slots = barbershop.get_available_slots(barber, date, service)
            if not slots:
                print(f"На {date_str} немає доступних слотів для {barber.name}.")
            else:
                print(f"\n=== ДОСТУПНІ СЛОТИ ДЛЯ {barber.name} НА {date_str} ===")
                for i, slot in enumerate(slots, 1):
                    print(f"{i}. {slot.strftime('%H:%M')}")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")

        input("\nНатисніть Enter, щоб продовжити...")

def handle_appointment_menu(barbershop):
    # Обробляє меню управління записами
    while True:
        print_appointment_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            # Перевірка наявності необхідних даних
            if not barbershop.customers:
                print("Немає жодного клієнта. Спочатку додайте клієнта.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            if not barbershop.barbers:
                print("Немає жодного фахівця. Спочатку додайте фахівця.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            if not barbershop.services:
                print("Немає жодної послуги. Спочатку додайте послугу.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            # Вибір клієнта
            print("\n=== СПИСОК КЛІЄНТІВ ===")
            for i, customer in enumerate(barbershop.customers, 1):
                print(f"{i}. {customer.__repr__()}")

            try:
                customer_idx = int(input("Виберіть номер клієнта: ")) - 1
                customer = barbershop.customers[customer_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            # Вибір фахівця
            print("\n=== СПИСОК ФАХІВЦІВ ===")
            for i, barber in enumerate(barbershop.barbers, 1):
                print(f"{i}. {barber.__repr__()}")

            try:
                barber_idx = int(input("Виберіть номер фахівця: ")) - 1
                barber = barbershop.barbers[barber_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            # Вибір послуги
            print("\n=== СПИСОК ПОСЛУГ ===")
            for i, service in enumerate(barbershop.services, 1):
                print(f"{i}. {service.__repr__()}")

            try:
                service_idx = int(input("Виберіть номер послуги: ")) - 1
                service = barbershop.services[service_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            # Введення дати
            date_str = input("Введіть дату (ДД-ММ-РРРР): ")
            date = parse_date(date_str)
            if not date:
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            # Перевірка доступності фахівця та отримання доступних слотів
            slots = barbershop.get_available_slots(barber, date, service)
            if not slots:
                print(f"На {date_str} немає доступних слотів для {barber.name}.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            # Вибір слоту
            print("\n=== ДОСТУПНІ СЛОТИ ===")
            for i, slot in enumerate(slots, 1):
                print(f"{i}. {slot.strftime('%H:%M')}")

            try:
                slot_idx = int(input("Виберіть номер слоту: ")) - 1
                slot = slots[slot_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            # Створення запису
            appointment = barbershop.create_appointment(customer, barber, service, slot)
            if appointment:
                print("Запис успішно створено!")
                print(appointment.__repr__())
            else:
                print("Не вдалося створити запис. Спробуйте ще раз.")

        elif choice == "2":
            # Скасування запису
            date_str = input("Введіть дату для перегляду записів (ДД-ММ-РРРР): ")
            date = parse_date(date_str)
            if not date:
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            appointments = barbershop.get_appointments_for_date(date)
            if not appointments:
                print(f"На {date_str} немає жодного запису.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            print("\n=== ЗАПИСИ НА ОБРАНУ ДАТУ ===")
            active_appointments = [a for a in appointments if a.status == "scheduled"]
            if not active_appointments:
                print(f"На {date_str} немає активних записів для скасування.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            for i, appointment in enumerate(active_appointments, 1):
                print(f"{i}. {appointment.__repr__()}")

            try:
                app_idx = int(input("Виберіть номер запису для скасування: ")) - 1
                appointment = active_appointments[app_idx]
                appointment.cancel()
                print("Запис успішно скасовано.")
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")

        elif choice == "3":
            # Позначення запису як виконаного
            date_str = input("Введіть дату для перегляду записів (ДД-ММ-РРРР): ")
            date = parse_date(date_str)
            if not date:
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            appointments = barbershop.get_appointments_for_date(date)
            if not appointments:
                print(f"На {date_str} немає жодного запису.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            print("\n=== ЗАПИСИ НА ОБРАНУ ДАТУ ===")
            active_appointments = [a for a in appointments if a.status == "scheduled"]
            if not active_appointments:
                print(f"На {date_str} немає активних записів для позначення як виконаних.")
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            for i, appointment in enumerate(active_appointments, 1):
                print(f"{i}. {appointment.__repr__()}")

            try:
                app_idx = int(input("Виберіть номер запису для позначення як виконаного: ")) - 1
                appointment = active_appointments[app_idx]
                appointment.complete()
                print("Запис успішно позначено як виконаний.")
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")

        elif choice == "4":
            # Перегляд записів на певну дату
            date_str = input("Введіть дату для перегляду записів (ДД-ММ-РРРР): ")
            date = parse_date(date_str)
            if not date:
                input("\nНатисніть Enter, щоб продовжити...")
                continue

            appointments = barbershop.get_appointments_for_date(date)
            if not appointments:
                print(f"На {date_str} немає жодного запису.")
            else:
                print(f"\n=== ЗАПИСИ НА {date_str} ===")
                for i, appointment in enumerate(appointments, 1):
                    status_text = {
                        "scheduled": "Заплановано",
                        "canceled": "Скасовано",
                        "completed": "Виконано"
                    }
                    status = status_text.get(appointment.status, appointment.status)
                    print(f"{i}. {appointment.__repr__()} - {status}")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")

        input("\nНатисніть Enter, щоб продовжити...")


def handle_barber_menu(barbershop):
    # Обробляє меню управління фахівцями
    while True:
        print_barber_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я фахівця: ")
            specialization = input("Введіть спеціалізацію фахівця (не обов'язково): ") or None

            barber = barbershop.add_barber(name, specialization)
            print(f"Фахівця {name} успішно додано!")

        elif choice == "2":
            if not barbershop.barbers:
                print("Немає жодного фахівця.")
            else:
                print("\n=== СПИСОК ФАХІВЦІВ ===")
                for i, barber in enumerate(barbershop.barbers, 1):
                    print(f"{i}. {barber.__repr__()}")

        elif choice == "3":
            if not barbershop.barbers:
                print("Спочатку додайте фахівця.")
                continue

            print("\n=== СПИСОК ФАХІВЦІВ ===")
            for i, barber in enumerate(barbershop.barbers, 1):
                print(f"{i}. {barber.name}")

            try:
                barber_idx = int(input("Виберіть номер фахівця: ")) - 1
                barber = barbershop.barbers[barber_idx]

                print(
                    "\nДні тижня: 1 - Понеділок, 2 - Вівторок, 3 - Середа, 4 - Четвер, 5 - П'ятниця, 6 - Субота, 7 - Неділя")
                day = int(input("Введіть день тижня (1-7): "))
                start_time = input("Введіть час початку роботи (HH:MM): ")
                end_time = input("Введіть час завершення роботи (HH:MM): ")

                if barber.set_working_hours(day, start_time, end_time):
                    print(f"Робочі години для {barber.name} на день {day} встановлено успішно!")
                else:
                    print("Не вдалося встановити робочі години. Перевірте правильність введених даних.")
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")

        elif choice == "4":
            if not barbershop.barbers:
                print("Немає жодного фахівця.")
                continue

            print("\n=== СПИСОК ФАХІВЦІВ ===")
            for i, barber in enumerate(barbershop.barbers, 1):
                print(f"{i}. {barber.name}")

            try:
                barber_idx = int(input("Виберіть номер фахівця: ")) - 1
                barber = barbershop.barbers[barber_idx]

                print("\n=== РОБОЧІ ГОДИНИ ===")
                for day, hours in barber.working_hours.items():
                    days = ["", "Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
                    start_time = hours[0].strftime("%H:%M")
                    end_time = hours[1].strftime("%H:%M")
                    print(f"{days[day]}: {start_time} - {end_time}")

            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")

        input("\nНатисніть Enter, щоб продовжити...")

def main():
    # Головна функція програми
    barbershop = BarberShop("BarberStyle")

    # Ініціалізація демонстраційних даних

    print(f"Ласкаво просимо до '{barbershop.name}'!")

    while True:
        print_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            handle_customer_menu(barbershop)
        elif choice == "2":
            handle_barber_menu(barbershop)
        elif choice == "3":
            handle_appointment_menu(barbershop)
        elif choice == "4":
            handle_schedule_menu(barbershop)
        elif choice == "0":
            print("Дякуємо за використання системи управління барбершопом!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
from datetime import datetime

class Service:
    # Клас, що представляє послугу в барбершопі з інформацією про тривалість та ціну
    def __init__(self, name, duration, price):
        # Ініціалізація нової послуги
        self.id = id(self)
        self.name = name
        self.duration = duration
        self.price = price

    def __str__(self):
        # Представлення об'єкта послуги у вигляді рядка
        return f"{self.name} ({self.duration} хв.) - {self.price} грн."


def clear_screen():
    # Очищає екран консолі
    print("\n" * 50)


def format_date(date_obj):
    # Форматує об'єкт дати у рядок
    return date_obj.strftime("%d.%m.%Y %H:%M")


def parse_date(date_str, format_str="%d.%m.%Y"):
    # Перетворює рядок дати в об'єкт datetime
    try:
        return datetime.strptime(date_str, format_str)
    except ValueError:
        print(f"Помилка: Некоректний формат дати. Використовуйте {format_str}")
        return None


def parse_days_range(days_input):
    # Перетворює рядок з діапазоном днів в список чисел
    days = []
    parts = days_input.split(",")

    for part in parts:
        if "-" in part:
            start, end = map(int, part.split("-"))
            days.extend(range(start, end + 1))
        else:
            days.append(int(part))

    return [day for day in days if 1 <= day <= 7]


def print_menu():
    # Виводить головне меню програми
    print("\n=== МЕНЮ БАРБЕРШОПУ ===")
    print("1. Управління клієнтами")
    print("2. Управління фахівцями")
    print("3. Управління послугами")
    print("4. Управління записами")
    print("5. Перегляд розкладу")
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


def print_service_menu():
    # Виводить меню управління послугами
    print("\n=== УПРАВЛІННЯ ПОСЛУГАМИ ===")
    print("1. Додати нову послугу")
    print("2. Переглянути всі послуги")
    print("3. Видалити послугу")
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
                    print(f"{i}.{customer}")

        elif choice == "3":
            phone = input("Введіть номер телефону для пошуку: ")
            customer = barbershop.find_customer_by_phone(phone)
            if customer:
                print(f"Знайдено клієнта: {customer}")
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
                        print(f"{i}. {appointment}")
            else:
                print("Клієнта з таким номером телефону не знайдено.")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


def handle_service_menu(barbershop):
    # Меню управління послугами
    while True:
        print_service_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть назву послуги: ")
            try:
                duration = int(input("Введіть тривалість послуги (хв): "))
                price = float(input("Введіть ціну послуги (грн): "))

                service = barbershop.add_service(name, duration, price)
                print(f"Послугу '{name}' успішно додано!")
            except ValueError:
                print("Помилка: Тривалість має бути цілим числом, а ціна - числом!")

        elif choice == "2":
            if not barbershop.services:
                print("Немає жодної послуги.")
            else:
                print("\n=== СПИСОК ПОСЛУГ ===")
                for i, service in enumerate(barbershop.services, 1):
                    print(f"{i}.{service}")

        elif choice == "3":
            if not barbershop.services:
                print("Немає жодної послуги для видалення.")
                continue

            print("\n=== СПИСОК ПОСЛУГ ===")
            for i, service in enumerate(barbershop.services, 1):
                print(f"{i}. {service}")

            try:
                idx = int(input("Виберіть номер послуги для видалення: ")) - 1
                if 0 <= idx < len(barbershop.services):
                    service = barbershop.services[idx]
                    barbershop.services.pop(idx)
                    print(f"Послугу '{service.name}' видалено.")
                else:
                    print("Неправильний індекс послуги.")
            except ValueError:
                print("Неправильний ввід. Введіть число.")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


def handle_schedule_menu(barbershop):
    # Обробляє меню перегляду розкладу
    while True:
        print_schedule_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            # Перегляд доступних фахівців на певну дату
            date_str = input("Введіть дату (ДД.ММ.РРРР): ")
            time_str = input("Введіть час (ГГ:ХХ): ")
            try:
                date = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M")
                available_barbers = barbershop.get_available_barbers(date)

                if not available_barbers:
                    print(f"На {date_str} о {time_str} немає доступних фахівців.")
                else:
                    print(f"\n=== ДОСТУПНІ ФАХІВЦІ НА {date_str} о {time_str} ===")
                    for i, barber in enumerate(available_barbers, 1):
                        print(f"{i}. {barber}")
            except ValueError:
                print("Помилка: Неправильний формат дати або часу.")

        elif choice == "2":
            # Перегляд доступних слотів для фахівця на певну дату
            if not barbershop.barbers:
                print("Немає жодного фахівця.")
                continue

            print("\n=== СПИСОК ФАХІВЦІВ ===")
            for i, barber in enumerate(barbershop.barbers, 1):
                print(f"{i}. {barber}")

            try:
                barber_idx = int(input("Виберіть номер фахівця: ")) - 1
                barber = barbershop.barbers[barber_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                continue

            if not barbershop.services:
                print("Немає жодної послуги. Слоти будуть показані для стандартної тривалості 30 хв.")
                service = None
            else:
                print("\n=== СПИСОК ПОСЛУГ ===")
                for i, service in enumerate(barbershop.services, 1):
                    print(f"{i}. {service}")

                try:
                    service_idx = int(input("Виберіть номер послуги (або 0 для стандартної тривалості): ")) - 1
                    service = None if service_idx < 0 else barbershop.services[service_idx]
                except (ValueError, IndexError):
                    print("Неправильний ввід. Буде використана стандартна тривалість 30 хв.")
                    service = None

            date_str = input("Введіть дату (ДД.ММ.РРРР): ")
            date = parse_date(date_str)
            if not date:
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


def handle_appointment_menu(barbershop):
    # Обробляє меню управління записами
    while True:
        print_appointment_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            # Перевірка наявності необхідних даних
            if not barbershop.customers:
                print("Немає жодного клієнта. Спочатку додайте клієнта.")
                continue

            if not barbershop.barbers:
                print("Немає жодного фахівця. Спочатку додайте фахівця.")
                continue

            if not barbershop.services:
                print("Немає жодної послуги. Спочатку додайте послугу.")
                continue

            # Вибір клієнта
            print("\n=== СПИСОК КЛІЄНТІВ ===")
            for i, customer in enumerate(barbershop.customers, 1):
                print(f"{i}. {customer}")

            try:
                customer_idx = int(input("Виберіть номер клієнта: ")) - 1
                customer = barbershop.customers[customer_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                continue

            # Вибір фахівця
            print("\n=== СПИСОК ФАХІВЦІВ ===")
            for i, barber in enumerate(barbershop.barbers, 1):
                print(f"{i}. {barber}")

            try:
                barber_idx = int(input("Виберіть номер фахівця: ")) - 1
                barber = barbershop.barbers[barber_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                continue

            # Вибір послуги
            print("\n=== СПИСОК ПОСЛУГ ===")
            for i, service in enumerate(barbershop.services, 1):
                print(f"{i}. {service}")

            try:
                service_idx = int(input("Виберіть номер послуги: ")) - 1
                service = barbershop.services[service_idx]
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")
                continue

            # Введення дати
            date_str = input("Введіть дату (ДД.ММ.РРРР): ")
            date = parse_date(date_str)
            if not date:
                continue

            # Перевірка доступності фахівця та отримання доступних слотів
            slots = barbershop.get_available_slots(barber, date, service)
            if not slots:
                print(f"На {date_str} немає доступних слотів для {barber.name}.")
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
                continue

            # Створення запису
            appointment = barbershop.create_appointment(customer, barber, service, slot)
            if appointment:
                print("Запис успішно створено!")
                print(appointment)
            else:
                print("Не вдалося створити запис. Спробуйте ще раз.")

        elif choice == "2":
            # Скасування запису
            date_str = input("Введіть дату для перегляду записів (ДД.ММ.РРРР): ")
            date = parse_date(date_str)
            if not date:
                continue

            appointments = barbershop.get_appointments_for_date(date)
            if not appointments:
                print(f"На {date_str} немає жодного запису.")
                continue

            print("\n=== ЗАПИСИ НА ОБРАНУ ДАТУ ===")
            active_appointments = [a for a in appointments if a.status == "scheduled"]
            if not active_appointments:
                print(f"На {date_str} немає активних записів для скасування.")
                continue

            for i, appointment in enumerate(active_appointments, 1):
                print(f"{i}. {appointment}")

            try:
                app_idx = int(input("Виберіть номер запису для скасування: ")) - 1
                appointment = active_appointments[app_idx]
                appointment.cancel()
                print("Запис успішно скасовано.")
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")

        elif choice == "3":
            # Позначення запису як виконаного
            date_str = input("Введіть дату для перегляду записів (ДД.ММ.РРРР): ")
            date = parse_date(date_str)
            if not date:
                continue

            appointments = barbershop.get_appointments_for_date(date)
            if not appointments:
                print(f"На {date_str} немає жодного запису.")
                continue

            print("\n=== ЗАПИСИ НА ОБРАНУ ДАТУ ===")
            active_appointments = [a for a in appointments if a.status == "scheduled"]
            if not active_appointments:
                print(f"На {date_str} немає активних записів для позначення як виконаних.")
                continue

            for i, appointment in enumerate(active_appointments, 1):
                print(f"{i}. {appointment}")

            try:
                app_idx = int(input("Виберіть номер запису для позначення як виконаного: ")) - 1
                appointment = active_appointments[app_idx]
                appointment.complete()
                print("Запис успішно позначено як виконаний.")
            except (ValueError, IndexError):
                print("Неправильний ввід. Спробуйте ще раз.")

        elif choice == "4":
            # Перегляд записів на певну дату
            date_str = input("Введіть дату для перегляду записів (ДД.ММ.РРРР): ")
            date = parse_date(date_str)
            if not date:
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
                    print(f"{i}. {appointment} - {status}")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")


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
                    print(f"{i}. {barber}")

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
                print(
                    "Приклади введення: '1-5' (з понеділка по п'ятницю), '1,3,5' (понеділок, середа, п'ятниця), '6-7' (вихідні)")
                days_input = input("Введіть дні тижня (наприклад, 1-5): ")
                days = parse_days_range(days_input)

                if not days:
                    print("Помилка: Не вказано жодного дня або неправильний формат")
                    continue

                start_time = input("Введіть час початку роботи (HH:MM): ")
                end_time = input("Введіть час завершення роботи (HH:MM): ")

                success = True
                for day in days:
                    if not barber.set_working_hours(day, start_time, end_time):
                        success = False
                        print(f"Помилка при встановленні робочих годин для дня {day}")

                if success:
                    print(f"Робочі години для {barber.name} на обрані дні встановлено успішно!")

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
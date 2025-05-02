#Модуль, що містить клас Schedule для управління розкладом барбершопу

from datetime import datetime, timedelta
from Appointment import Appointment


class Schedule:
    #Клас, що управляє розкладом барбершопу, доступністю фахівців та створенням записів
    def __init__(self):
        #Ініціалізація нового розкладу
        self.barbers = []

    def add_barber(self, barber):
        #Додає фахівця до розкладу
        if barber not in self.barbers:
            self.barbers.append(barber)

    def remove_barber(self, barber):
        #Видаляє фахівця з розкладу
        if barber in self.barbers:
            self.barbers.remove(barber)

    def get_available_barbers(self, date):
        #Повертає список доступних фахівців на певну дату і час
        available_barbers = []
        for barber in self.barbers:
            if barber.is_available_at(date):
                available_barbers.append(barber)
        return available_barbers

    def get_available_slots(self, barber, date, duration=30):
        #Повертає доступні часові слоти для фахівця на певну дату

        available_slots = []

        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                print("Помилка: Некоректний формат дати. Використовуйте DD-MM-YYYY")
                return available_slots

        day_of_week = date.isoweekday()

        if day_of_week not in barber.working_hours:
            return available_slots

        working_start, working_end = barber.working_hours[day_of_week]

        current_slot = datetime.combine(date.date(), working_start)
        end_time = datetime.combine(date.date(), working_end)

        while current_slot + timedelta(minutes=duration) <= end_time:
            if barber.is_available_at(current_slot):
                slot_end = current_slot + timedelta(minutes=duration)
                is_slot_available = True

                test_time = current_slot
                while test_time < slot_end:
                    if not barber.is_available_at(test_time):
                        is_slot_available = False
                        break
                    test_time += timedelta(minutes=5)

                if is_slot_available:
                    available_slots.append(current_slot)

            current_slot += timedelta(minutes=30)

        return available_slots

    def create_appointment(self, customer, barber, service, date):
        #Створює новий запис на послугу

        if not isinstance(date, datetime):
            try:
                date = datetime.strptime(date, "%d-%m-%Y %H:%M")
            except ValueError:
                print("Помилка: Некоректний формат дати. Використовуйте DD-MM-YYYY HH:MM")
                return None

        if not self._validate_date_time(date):
            return None

        if not barber.is_available_at(date):
            print(f"Помилка: Фахівець {barber.name} недоступний у вказаний час")
            return None

        slot_end = date + timedelta(minutes=service.duration)
        is_slot_available = True

        test_time = date
        while test_time < slot_end:
            if not barber.is_available_at(test_time):
                is_slot_available = False
                break
            test_time += timedelta(minutes=5)

        if not is_slot_available:
            print("Помилка: Недостатньо часу для надання послуги")
            return None

        appointment = Appointment(customer, barber, service, date)

        customer.add_appointment(appointment)
        barber.add_appointment(appointment)

        return appointment

    def _validate_date_time(self, date):
        #Валідує дату і час для створення запису
        if not isinstance(date, datetime):
            print("Помилка: Дата та час мають бути об'єктом datetime")
            return False

        if date < datetime.now():
            print("Помилка: Неможливо створити запис на минулу дату")
            return False

        max_date = datetime.now() + timedelta(days=90)
        if date > max_date:
            print("Помилка: Запис можливий не більше ніж на 3 місяці вперед")
            return False

        return True
from datetime import datetime, timedelta


class Customer:

    def __init__(self, name, phone, email=None):
        self.id = id(self)
        self.name = name
        self._phone = None
        self.set_phone(phone)
        self.email = email
        self.appointments = []

    def set_phone(self, phone):
        cleaned_phone = ''.join(filter(str.isdigit, str(phone)))

        if len(cleaned_phone) == 10 or len(cleaned_phone) == 12:
            self._phone = cleaned_phone
        else:
            print("Помилка: Некоректний формат номера телефону")
            return False
        return True

    @property
    def phone(self):
        return self._phone

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def get_appointments(self):
        return self.appointments

    def __str__(self):
        return f"Клієнт: {self.name}, Телефон: {self._phone}"


class Barber:

    def __init__(self, name, specialization=None):
        self.id = id(self)
        self.name = name
        self.specialization = specialization
        self.working_hours = {}
        self.appointments = []

    def set_working_hours(self, day_of_week, start_time, end_time):
        if 1 <= day_of_week <= 7:
            if isinstance(start_time, str):
                start_time = datetime.strptime(start_time, "%H:%M").time()
            if isinstance(end_time, str):
                end_time = datetime.strptime(end_time, "%H:%M").time()

            if start_time < end_time:
                self.working_hours[day_of_week] = [start_time, end_time]
                return True
            else:
                print("Помилка: Час завершення має бути після часу початку")
                return False
        else:
            print("Помилка: День тижня має бути числом від 1 до 7")
            return False

    def is_available_at(self, datetime_obj):
        day_of_week = datetime_obj.isoweekday()

        if day_of_week not in self.working_hours:
            return False

        working_start, working_end = self.working_hours[day_of_week]
        current_time = datetime_obj.time()

        if not (working_start <= current_time < working_end):
            return False

        for appointment in self.appointments:
            if appointment.date.date() == datetime_obj.date():
                app_start = appointment.date
                app_end = appointment.date + timedelta(minutes=appointment.duration)

                if app_start <= datetime_obj < app_end:
                    return False

        return True

    def add_appointment(self, appointment):
        self.appointments.append(appointment)
        self.appointments.sort(key=lambda a: a.date)

    def get_appointments_for_date(self, date):
        return [a for a in self.appointments if a.date.date() == date.date()]

    def __str__(self):
        return f"Фахівець: {self.name}, Спеціалізація: {self.specialization}"


class Service:

    def __init__(self, name, duration, price):
        self.id = id(self)
        self.name = name
        self.duration = duration
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.duration} хв.) - {self.price} грн."


class Appointment:

    def __init__(self, customer, barber, service, date):
        self.id = id(self)
        self.customer = customer
        self.barber = barber
        self.service = service
        self._date = None
        self.duration = service.duration
        self.set_date(date)
        self.status = "scheduled"

    def set_date(self, date):
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%d-%m-%Y %H:%M")
            except ValueError:
                print("Помилка: Некоректний формат дати. Використовуйте DD-MM-YYYY HH:MM")
                return False

        if not isinstance(date, datetime):
            print("Помилка: Дата має бути об'єктом datetime")
            return False

        if date < datetime.now():
            print("Помилка: Неможливо створити запис на минулу дату")
            return False

        self._date = date
        return True

    @property
    def date(self):
        return self._date

    def cancel(self):
        self.status = "canceled"

    def complete(self):
        self.status = "completed"

    def __str__(self):
        date_str = self.date.strftime("%d-%m-%Y %H:%M")
        return f"Запис #{self.id}: {self.customer.name} на {date_str} до {self.barber.name}, Послуга: {self.service.name}"
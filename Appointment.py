from datetime import datetime

class Appointment:
    #Клас, що представляє запис клієнта на послугу до фахівця у певний час

    def __init__(self, customer, barber, service, date):
        #Ініціалізація нового запису
        self.id = id(self)
        self.customer = customer
        self.barber = barber
        self.service = service
        self._date = None
        self.duration = service.duration
        self.set_date(date)
        self.status = "scheduled"

    def set_date(self, date):
        #Встановлює і валідує дату запису
        if isinstance(date, str):
            try:
                date = datetime.strptime(date, "%d.%m.%Y %H:%M")
            except ValueError:
                print("Помилка: Некоректний формат дати. Використовуйте DD.MM.YYYY HH:MM")
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
        #Повертає дату і час запису
        return self._date

    def cancel(self):
        #Скасовує запис
        self.status = "canceled"

    def complete(self):
        #Позначає запис як виконаний
        self.status = "completed"

    def __str__(self):
        # Представлення об'єкта запису у вигляді рядка
        date_str = self.date.strftime("%d.%m.%Y %H:%M")
        return f"Запис #{self.id}: {self.customer.name} на {date_str} до {self.barber.name}, Послуга: {self.service.name}"
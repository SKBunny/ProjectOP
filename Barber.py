#Модуль, що містить клас Barber для управління даними про фахівців барбершопу
from datetime import datetime, timedelta

class Barber:
    #Клас, що представляє фахівця барбершопу з його даними, розкладом та записами
    def __init__(self, name, specialization=None):
        #Ініціалізація нового фахівця.
        self.id = id(self)
        self.name = name
        self.specialization = specialization
        self.working_hours = {}
        self.appointments = []

    def set_working_hours(self, day_of_week, start_time, end_time):
        #Встановлює робочі години фахівця на певний день тижня
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
        #Перевіряє доступність фахівця в конкретний час
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
        #Додає новий запис до розкладу фахівця
        self.appointments.append(appointment)
        self.appointments.sort(key=lambda a: a.date)

    def get_appointments_for_date(self, date):
        #Повертає всі записи фахівця на певну дату
        return [a for a in self.appointments if a.date.date() == date.date()]

    def __repr__(self):
        #Представлення об'єкта фахівця у вигляді рядка
        return f"Фахівець: {self.name}, Спеціалізація: {self.specialization}"
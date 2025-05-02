#Модуль, що містить клас Customer для управління даними клієнтів барбершопу
from datetime import datetime

class Customer:
    #Клас, що представляє клієнта барбершопу з його персональними даними та записами

    def __init__(self, name, phone, email=None):
        #Ініціалізація нового клієнта

        self.id = id(self)
        self.name = name
        self._phone = None
        self.set_phone(phone)
        self.email = email
        self.appointments = []

    def set_phone(self, phone):
        #Встановлює та валідує номер телефону клієнта

        cleaned_phone = ''.join(filter(str.isdigit, str(phone)))

        if len(cleaned_phone) == 10 or len(cleaned_phone) == 12:
            self._phone = cleaned_phone
        else:
            print("Помилка: Некоректний формат номера телефону")
            return False
        return True

    @property
    def phone(self):
        #Повертає номер телефону клієнта
        return self._phone

    def add_appointment(self, appointment):
        #Додає новий запис до списку записів клієнта
        self.appointments.append(appointment)

    def get_appointments(self):
        #Повертає всі записи клієнта
        return self.appointments

    def __repr__(self):
        #Представлення об'єкта клієнта у вигляді рядка
        return f"Клієнт: {self.name}, Телефон: {self._phone}"
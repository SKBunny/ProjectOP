from Customer import Customer
from Barber import Barber
from Service import Service
from Schedule import Schedule


class BarberShop:
    #Клас, що представляє барбершоп з управлінням клієнтами, фахівцями, послугами та записами
    def __init__(self, name):
        #Ініціалізація нового барбершопу

        self.name = name
        self.customers = []
        self.barbers = []
        self.services = []
        self.schedule = Schedule()

    def add_customer(self, name, phone, email=None):
        #Додає нового клієнта до барбершопу
        customer = Customer(name, phone, email)
        if customer.phone:
            self.customers.append(customer)
            return customer
        return None

    def add_barber(self, name, specialization=None):
        #Додає нового фахівця до барбершопу
        barber = Barber(name, specialization)
        self.barbers.append(barber)
        self.schedule.add_barber(barber)
        return barber

    def add_service(self, name, duration, price):
        #Додає нову послугу до барбершопу
        service = Service(name, duration, price)
        self.services.append(service)
        return service

    def find_customer_by_phone(self, phone):
        #Шукає клієнта за номером телефону
        cleaned_phone = ''.join(char for char in str(phone) if char.isdigit())
        for customer in self.customers:
            if customer.phone == cleaned_phone:
                return customer
        return None

    def get_available_barbers(self, date):
        #Повертає список доступних фахівців на певну дату і час
        return self.schedule.get_available_barbers(date)

    def get_available_slots(self, barber, date, service=None):
        #Повертає доступні часові слоти для фахівця на певну дату
        duration = service.duration if service else 30
        return self.schedule.get_available_slots(barber, date, duration)

    def create_appointment(self, customer, barber, service, date):
        #Створює новий запис на послугу
        return self.schedule.create_appointment(customer, barber, service, date)

    def get_appointments_for_date(self, date):
        #Повертає всі записи на певну дату
        appointments = []
        for barber in self.barbers:
            appointments.extend(barber.get_appointments_for_date(date))
        return appointments
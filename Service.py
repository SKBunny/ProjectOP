#Модуль, що містить клас Service для управління послугами барбершопу

class Service:
    #Клас, що представляє послугу в барбершопі з інформацією про тривалість та ціну
    def __init__(self, name, duration, price):
        #Ініціалізація нової послуги
        self.id = id(self)
        self.name = name
        self.duration = duration
        self.price = price

    def __repr__(self):
        #Представлення об'єкта послуги у вигляді рядка
        return f"{self.name} ({self.duration} хв.) - {self.price} грн."
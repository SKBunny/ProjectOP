# ProjectOP
Система управління барбершопом "Frisor"
Програма для повного управління роботою барбершопу: клієнти, фахівці, послуги, записи та розклад.
Опис проєкту
Система управління барбершопом "Frisor" - це консольний додаток на Python для ефективного управління роботою барбершопу. Система допомагає організувати роботу закладу, керувати клієнтською базою, планувати розклад фахівців та контролювати записи клієнтів на послуги.
Функціональність
1. Управління клієнтами
Додавання нових клієнтів з валідацією контактних даних
Перегляд списку всіх клієнтів
Пошук клієнтів за номером телефону
Перегляд усіх записів конкретного клієнта

2. Управління фахівцями (барберами)
Додавання нових фахівців із зазначенням спеціалізації
Перегляд списку всіх фахівців
Налаштування індивідуального графіку роботи для кожного фахівця
Перегляд розкладу роботи фахівця

3. Управління послугами
Додавання нових послуг з вказанням тривалості та вартості
Перегляд списку всіх доступних послуг
Видалення послуг з каталогу

4. Управління записами
Створення нових записів клієнтів з перевіркою доступності фахівців
Скасування записів
Позначення записів як виконаних
Перегляд всіх записів на певну дату

5. Управління розкладом
Перегляд доступних фахівців на конкретну дату та час
Пошук доступних часових слотів для запису на певну дату

Структура проєкту

main.py - головний модуль програми з консольним інтерфейсом
barbershop.py - клас BarberShop для управління барбершопом
Customer.py - клас Customer для управління даними клієнтів
Barber.py - клас Barber для управління даними фахівців та їх розкладом
Service.py - клас Service для управління послугами та функції інтерфейсу користувача
Schedule.py - клас Schedule для управління розкладом барбершопу
Appointment.py - клас Appointment для управління записами клієнтів





############################################################

# class Customer:
#     def __init__(self, name: str):
#         self.name = name
#         # Добавьте сюда приватный атрибут "скидка"
#         # со значением по умолчанию 10.
#         self.__discount = 10

#     # Метод set_discount() принимает на вход
#     # новое значение для приватного атрибута "скидка".
#     # Если new_value превышает 80 -
#     # новое значение скидки должно стать 80.
#     # Метод не должен ничего возвращать.
#     def set_discount(self, new_value: int):
#         if new_value >80:
#             self.__discount = 80
#         else:
#             self.__discount = new_value
#     # Метод get_price() получает на вход исходную стоимость товара
#     # и должен вернуть новую цену товара с учётом
#     # скидки покупателя.
#     # Возвращаемое значение округлите до двух знаков после запятой.
#     def get_price(self, price: int) -> float:
#         dis_price = round((price - (price * self.__discount/100)),2)
#         return dis_price


# # Проверим работу программы.
# # Создаём объект покупателя:
# customer = Customer('Иван Иванович')

# original_price = 85

# print(
#     f'С исходной скидкой Иван Иванович заплатит '
#     f'{customer.get_price(original_price)} рублей вместо {original_price}'
# )
# # Изменим скидку до неприемлемого уровня.
# # Метод set_discount() должен установить размер скидки равным 80.
# customer.set_discount(90)
# print(
#     f'С новой скидкой Иван Иванович заплатит '
#     f'{customer.get_price(original_price)} рублей вместо {original_price}'
# )



######################################################################

# # Импортируйте нужную библиотеку.
# from datetime import datetime

# class Store:
#     def __init__(self, address):
#         self.address: str = address

#     def __is_open(self, date) -> bool:
#         # Метод __is_open() в родительском классе всегда возвращает False,
#         # это "код-заглушка", метод, предназначенный для переопределения
#         # в дочерних классах.
#         # Не переопределяйте содержимое этого метода.
#         return False

#     def get_info(self, text_date) -> str:
#         # С помощью шаблона даты преобразуйте строку date_str в объект даты:
#         date_object = datetime.strptime(text_date, '%d.%m.%Y')

#         # Передайте в метод __is_open() объект даты date_object и определите,
#         # работает ли магазин в указанную дату.
#         # В зависимости от результата будет выбрано значение
#         # для переменной info.
#         if self.__is_open(date_object):
#             info = 'работает'
#         else:
#             info = 'не работает'
#         return f'Магазин по адресу {self.address} {text_date} {info}'


# class MiniStore(Store):
#     # Переопределите метод __is_open().
#     # Обратите внимание на имя метода/name mangling
#     def _Store__is_open(self, date: datetime) -> bool:
#         weekday = date.weekday()
#         return weekday != 5 and weekday !=6 # можно также через weekday<5



# class WeekendStore(Store):
#     # Переопределите метод __is_open().
#     # Обратите внимание на имя метода/name mangling
#     def _Store__is_open(self, date: datetime) -> bool:
#         weekday = date.weekday()
#         return weekday == 5 or weekday == 6


# class NonStopStore(Store):
#     # Переопределите метод __is_open().
#     # Обратите внимание на имя метода/name mangling
#     def _Store__is_open(self, date: datetime) -> bool:
#         return True


# mini_store = MiniStore('Улица Немига, 57')
# print(mini_store.get_info('06.04.2024'))
# print(mini_store.get_info('30.03.2024'))

# weekend_store = WeekendStore('Улица Толе би, 321')
# print(weekend_store.get_info('29.03.2024'))
# print(weekend_store.get_info('30.03.2024'))

# non_stop_store = NonStopStore('Улица Арбат, 60')
# print(non_stop_store.get_info('29.03.2024'))
# print(non_stop_store.get_info('30.03.2024'))



###############################################################

# class Employee:
#     vacation_days: int = 28

#     def __init__(
#         self,
#         first_name: str,
#         last_name: str,
#         gender: str,
#     ):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.remaining_vacation_days = self.vacation_days
#         self._employee_id = self.__generate_employee_id()

#     def consume_vacation(self, days: int):
#         self.remaining_vacation_days -= days
        

#     def __generate_employee_id(self): 
#         return hash(self.first_name + self.last_name + self.gender)


#     def get_remaining_vacation_days(self) -> int:
#         return self.remaining_vacation_days


# class OfficeEmployee(Employee):
#     def __init__(
#         self,
#         first_name: str,
#         last_name: str,
#         gender: str,
#         worker_class: int,
#         salary: int
#     ):
#         self.worker_class = worker_class
#         self.__salary = salary
#         super().__init__(first_name, last_name, gender)
#         self.remaining_vacation_days = self.vacation_days + self.worker_class * 2
        
#     def get_vacation_payment(self, days) -> int:
#         return int(days * (self.__salary/60))
    


# # Пример использования:
# office_employee = OfficeEmployee(
#     first_name='Иван',
#     last_name='Иванов',
#     gender='м',
#     worker_class=2,
#     salary=45000
# )

# vacation_days = 10


# office_employee.consume_vacation(vacation_days)

# remaining_days = office_employee.get_remaining_vacation_days()
# print(f'У сотрудника осталось {remaining_days} дн. отпуска.')

# vacation_payment = office_employee.get_vacation_payment(vacation_days)
# print(f'За {vacation_days} дн. отпуска сотрудник получит {vacation_payment} руб.')


####################################################


# class Employee:
#     vacation_days = 28

#     def __init__(self, first_name, second_name, gender):
#         self.first_name = first_name
#         self.second_name = second_name
#         self.gender = gender
#         self.remaining_vacation_days = self.vacation_days

#     def consume_vacation(self, days):
#         self.remaining_vacation_days -= days

#     def get_vacation_details(self):
#         return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
    
# class FullTimeEmployee(Employee):


#     def __init__(self, first_name, second_name, gender, pound):
#         self.pound = pound

#     def get_unpaid_vacation(self, begin_date, volume):
#         return f'Начало неоплачиваемого отпуска: {begin_date}, продолжительность: {volume} дней.'
    
# class PartTimeEmployee(Employee):
#     vacation_days = 14

# full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
# print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
# part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
# print(part_time_employee.get_vacation_details())













# class Phone:

#     line_type = 'проводной'

#     def __init__(self, dial_type_value):
#         self.dial_type = dial_type_value

#     def ring(self):
#         print('Дзззззыыыыыыыынь!')

#     def call(self, phone_number):
#         print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

# class MobilePhone(Phone):
#     line_type = 'беспроводной'
#     battery_type = 'Li-ion'

#     # Инициализатор класса MobilePhone с новым параметром - network_type.
#     def __init__(self, network_type):
#         # Вызов родительского инициализатора.
#         super().__init__(dial_type_value)
#         # Новый атрибут объекта.
#         self.network_type = network_type

#     def ring(self):
#         print('Дзынь-дзынь!')


# router = MobilePhone('сенсорный','GSM')

# print(router.network_type)

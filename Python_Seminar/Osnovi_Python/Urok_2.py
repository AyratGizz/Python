# Настройка среды разработки Python для Windows
# Установка PyCharm
# Переменные. Типы данных, преобразование типов
# name = 'Кеша'
# age = 2
# period = 2
# print("Попугайчик", name, "в", age, " года научился говорить своё имя", name)
# --- --- --- Тип переменной--- --- --- --- ---
# int - целое число
# float - число с плавающей точкой
# bool - логический тип (истина - True /ложь - False)
# None - ничего (пустой тип)
# str - строка
# name = 'Айрат'
# print(type(name), name)  # type - определение типа данных
# stroka = '36'
# print(type(stroka), stroka)
# stroka = int(stroka)
# print(type(stroka), stroka)
# Вывод в консоль (терминал)
# print('Привет', name, '!', sep='**')  # sep - сепаратор - склеиватель
# print('Привет', name, end='!')
# Ввод данных
# name = input('Введите своё имя: ')
# print('Привет', name)
#
# age = int(input('Сколько вам лет?: '))
# period = 20
# age_period = age + period
# print('Через', period, 'лет, вам будет', age_period)
# --------- Арифметические и логические операции.-----------------
# Соответствие нескольким условиям and, or, not
# Арифметические операции
# + - сложение
# - - вычитание
# * - умножение
# / - деление
# // - целая часть от деления (получение целого числа при делении - всегда int )
# % - остаток от деления (получение остатка от деления -  всегда float)
# ** - возведение в степень - 2**10 - 2 в степени 10

# Приоритет арифметических операций - Умножение и деление в приоритете

# Логические операции (получаем bool значение - True, False)
# == (= =) - равно
# != - (! = ) - не равно
# > - больше
# < - меньше
# >= (> =) - больше или равно
# <= (< =) - меньше или равно

# Сложные логические выражения (получаем bool значение - True, False)
# and - и (ИСТИНА когда все ИСТИНА иначе ЛОЖЬ)
# or - или (ЛОЖЬ когда все ЛОЖЬ иначе ИСТИНА
# not - не (ИСТИНА когда ЛОЖЬ, ЛОЖЬ когда ИСТИНА)

# ----------- Условные операторы ---------------
# --------
# --- if - ЕСЛИ
# --- elif - "ИЛИ" ЕСЛИ
# --- else - ИНАЧЕ
# age = int(input('Введите ваш возраст: '))
# if age > 18:
#     print('Доступ разрешён')
# elif age == 18:
#     print('Ура вам 18 лет! Добро пожаловать!')
# else:
#     print('Доступ запрещен')
# --------
# number = 43
# value = int(input('Введите число от 1 до 100: '))
# while value != number:
#     if value > number:
#         print('Нужно меньше')
#         value = int(input('Введите число от 1 до 100: '))
#     else:
#         print('Нужно больше')
#         value = int(input('Введите число от 1 до 100: '))
# print('Вы угадали!')
# -------------------- Циклы ----------------------------------
# while - Условие - "Пока"
# name = input('Кто создатель Python?: ')
# while name != 'Гвидо':
#     print('НЕ верно!')
#     name = input('Кто создатель Python?: ')
# print('Правильно!')
# Вывод чисел от 0 до 100
# number = 0
# n = int(input('Введите n: '))
# while number <= n:
#     print(number)
#     number += 1
# Вывод только четных чисел
# number = 0
# n = int(input('Введите n: '))
# while number <= n:
#     if number % 2 == 0:
#         print(number)
#     number += 1
# Вывод только нечетных чисел
# number = 0
# n = int(input('Введите n: '))
# while number <= n:
#     if number % 2 != 0:
#         print(number)
#     number += 1
# --------- Break----------
# break - выход условия не зависимо от выполнения условия
# name = None
# while True:  # было - name != 'Гвидо'
#     name = input('Кто создатель Python?: ')
#     if name == 'Гвидо':
#         break
#     print('НЕ верно!')
# print('Правильно!')
# --------- Continue --------
# continue - Переход на следующую итерацию цикла (команды в цикле после команды не выполняются)
# number = 0
# n = int(input('Введите n: '))
# while number <= n:
#     if number % 2 == 0:
#         number += 1
#         continue
#     print(number)
#     number += 1
# ----- Else в цикле While ----------------
# number = 0
# while number <= 100:
#     print(number)
#     number += 1
#     # if number == 33:
#     #     break
# else:
#     print('else - end')
# print('end')
#
#
#
#
#

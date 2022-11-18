# Пользователь вводит 3 числа. Найти минимальное из них,
#  максимальное из них, их сумму и вывести результат на экран.
# count = int(input('Сколько будет чисел?: '))
# numbers = []
# for i in range(count):
#     number = int(input(f'Введите {i + 1} число : '))
#     numbers.append(number)
#
# print('Максимальное число =', max(numbers))
# print('Минимальное число =', min(numbers))
# print('Сумма всех чисел =', sum(numbers))
# -------------------------------------------------------------------------------------------
# ----- Создание своей функции -----
# def get_sep(sep, sep_len):
#     return sep * sep_len
#
#
# sep = get_sep('*', 20)
# text = 'Привет {} Func {}'.format(sep, sep)
# print(text)
# -------------------------------------------------------------------------------------------
# def hello_max():
#     print('Hello Max')
#
#
# hello_max()
#
#
# def hello(who):
#     print('Hello', who)
#
#
# hello('Leo')
#
#
# def greeting(who, say='Hello'):
#     print(say, who)
#
#
# greeting(say='Leo', who='Privet')
# greeting('Leo')
#
#
# def greeting(say, *args):
#     print(say, args)
#
#
# greeting('Hello', 'Leo', 'Max', 'Kate')
#
#
# def greeting(**kwargs):
#     for k, v in kwargs.items():  # k - ключ, v - значение
#         print(k, v)
#
#
# greeting(name='Leo', age=20)
# -----------------------------------------------------------------------------------------------------
# ---------------------------------- Функции в функциях -------------------------------
# def some_f():
#     return 10
#
#
# result = some_f()
# print(result)
#
# a = some_f  # Переменная стала функцией "some_f"
# print(a)
#
# print(type(a))
# print(a())
# ------------------------------------
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number):
#             result.append(number)
#     return result
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# def is_even(number):
#     return number % 2 == 0
#
#
# print(my_filter(numbers, is_even))
#
#
# def is_not_even(number):
#     return number % 2 != 0
#
#
# print(my_filter(numbers, is_not_even))
#
#
# def big_for(number):
#     return number > 4
#
#
# print(my_filter(numbers, big_for))
# ---------------------------------- Lambda функции ---------------------------------------------
# Тоже самое что сверху, только в lambda функции и не хотим давать имя функции и писать её отдельно!
# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number):
#             result.append(number)
#     return result
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# print(my_filter(numbers, lambda number: number % 2 == 0))
# print(my_filter(numbers, lambda number: number % 2 != 0))
# print(my_filter(numbers, lambda number: number > 4))
# -----------------------------------------------------------------------------------------------
# ------------ Встроенные полезные функции sorted, filter, map ----------------------------------
# -------------------------- sorted -----------------------
# Сортировка последовательности по алфавиту и т.п.
# numbers = [1, 5, 3, 5, 9, 7, 11]
# print(sorted(numbers))  # Сортировка по возрастанию
# print(sorted(numbers, reverse=True))  # Сортировка по убыванию
# # Как отсортировать не по алфавиту, а по второму числу (численности)
# cities = [('Moscow', 1000), ('LasVegas', 500), ('Michigan', 2000)]
# print(sorted(cities))  # Сортировка по алфавиту
#
#
# # Сортировка по ключу
# def by_count(city):
#     return city[1]
#
#
# print(sorted(cities, key=by_count))
# # Можно использовать lambda
# print(sorted(cities, key=lambda city: city[1]))
# ----------------------- filter ------------------------------
# Фильтрация последовательности
# Принимает 2 параметра - функция и последовательность
# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
#
#
# def is_even(number):
#     return number % 2 == 0
#
#
# result = filter(is_even, numbers)
# print(result)
# result = list(result)
# print(result)
#
# names = ['Max', 'Leo', 'Kate']
#
# print(list(filter(lambda x: len(x) > 3, names)))  # В имени больше 3 символов
# ------------------------ Функция map----------------------------
# Применяется к каждому элементу последовательности
# Имеет 2 аргумента - функция и - последовательность
numbers = [5, 3, 4, 7, 8]
print(list(map(lambda x: x ** 2, numbers)))  # Возведение чисел в квадрат
print(list(map(lambda x: str(x), numbers)))  # Приведение к строке
# #

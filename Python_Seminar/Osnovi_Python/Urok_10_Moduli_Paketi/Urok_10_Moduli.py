# Определение модуля
# Модулем в Python называется любой файл с программой
# Используются для повторного использования кода
# Используется для управления пространством имен
# Используется для деления проекта на мелкие части
# --- Разновидности модулей ---
# 1. Встроенные (math, random ...)
# 2. Сторонние (django, PyQT5, ...)
# 3. Свои созданные модули
# --- Варианты подключения ---
# 1. Модуль целиком (import math)
# 2. Псевдоним для модуля (import math as mt)
# 3. Импорт всего содержания (from math import *
# 4. Импорт конкретных функций, классов ... (from math import sin, cos)
# ------------------------------------------------------------------------------------------
# import math
# import random as rd
#
# print(math.pi)
# print(math.sin(38))
# print(rd.randint(1, 10))

# ----------
# from math import *
# from random import randint, randrange
#
# print(pi)
# print(sin(38))
# print(randint(1, 10))
# --------------------------------------------------------------------------------------------
# ------- Библиотека Math ------------
# factorial
# exp
# log, log2, log10
# sqrt
# sin, cos, asin, acos, ...
# и др...
# import math
#
# # 1. найти длину окружности с определенным радиусом
# r = 100
# print(2 * r * math.pi)
# # 2. Найти площадь окружности с определенным радиусом
# print((r ** 2) * math.pi)
# print(math.pow(r, 2) * math.pi)
# # 3. По координатам 2-х точек определить расстояние между ними
# x1 = 10
# y1 = 10
# x2 = 50
# y2 = 100
# l = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# print(l)
# # 4. Найти факториал числа 9
# print(math.factorial(9))
# ---------------- Модуль RANDOM -------------------
# randint - целое число от А до В
# choise - случайный элемент последовательности
# shuffle - перемешивание последовательности
# random - случайной число от 0 до 10000000
# sample - список длиной k из последовательности
# и др...
# 1. Загадать случайное число от 0 до 100
# from random import randint, choice, sample, shuffle
#
# print(randint(0, 100))
# # 2. Выбрать победителя лотереи из списка players
# players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
# print(choice(players))
# # 3. Выбрать 3-х победителей лотерей из списка players
# print(sample(players, 3))
# # 4. Перемешать карты в стопке (списке) cards
# cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# print(cards)
# shuffle(cards)
# print(cards)
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------ Функции и переменные OS -----------------------------------------------
# name - имя операционной системы
# chdir - смена текущей директории
# getcwd() - текущая рабочая директория
# mkdir() - создание директории (папки)
# os.path - модуль для работы с путями
# и др...
# import os
#
# print(os.name)
# print(os.getcwd())
# new_patch = os.path.join(os.getcwd(), 'new_f')
# os.mkdir(new_patch)
# ------------------------------------- Модули SYS -----------------------------------------------------------
# - Взаимодействие с интерпретатором python
# ------ Функции и переменные SYS --------
# executable - путь к интерпретатору python
# exit() - выход из python
# platform - информация об ОС
# path - список путей поиска модулей
# argv - список аргументов командной строки
# и др...
# import sys
#
# print(sys.executable)
# print(sys.platform)
# sys.exit()
# print('Этот код мы уже не выполним, так как вышли...')
# ---------- sys.path ---------------
# Очень важная переменная
# Она хранит пути по которым python ищет модули.
# Она имеет изменяемый тип данных list
# таким образом мы можем изменять эту переменную
# import math
#
# import sys
#
# print(sys.path)
# print(type(sys.path))
#
# for p in sys.path:
#     print(p)
# sys.path.append('D:')
# import mymodule
# Пример для тренировки
# В паке с модулем создать 5 подпапок названия которых состоят из платформы на которой
# запущен интерпретатор и порядкового номера начания с 1: win32_1, win32_2, ... Платформа может
# быть другой.
# import os
# import sys
#
# name = sys.platform
#
# for i in range(1, 6):
#     new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
#     os.mkdir(new_path)
# ------ sys.argv --------
# Список аргументов командной строки при запуске скрипта python
# sys.argv[0] - путь до скрипта
# Остальные параметры передаются при вызове скрипта через пробел
# например: python my_script.py par1 par2 par3....
# import sys
#
# for arg in sys.argv:
#     print(arg)
# ------------------------------------------------------------------------------------------------------
import sys
import os


def ping():
    print('pong')


def hello(name):
    print('Hello', name)


hello('Leo')


def get_info():
    print(os.listdir())


command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)

#
# #

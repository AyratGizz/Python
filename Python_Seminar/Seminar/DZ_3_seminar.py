## № 22 - Задайте список из нескольких чисел. Напишите программу, 
## которая найдёт сумму элементов списка, стоящих на нечётной позиции.
## Пример:
## - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
## ----Разбор задачи на семинаре № 4------------------

# count = int(input('Введите количесвто элементов списка: '))
# some_list = []
# summa = 0

# for i in range (count):
#     number = int(input(f'Введите число позиции списка {i}: '))
#     some_list.append(number)

# for i in range(1, count, 2): # Третий аргумент - шаг начиная c 1, далее 3 , 5 и т.д.
#     summa += some_list[i]
# print(summa)

## - Сдано мной на платформе --------------
# x = [2, 3, 6, 10, 12, 16, 5]
# #print(x)
# summ = 0
# for i in range(1, len(x), 2):
#     #if i % 2 == 1:
#         summ += x[i]       
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")

## ------------------------------------------------------------------
## № 23 - Напишите программу, которая найдёт произведение пар чисел списка. 
## Парой считаем первый и последний элемент, второй и предпоследний и т.д.
## Пример:
## - [2, 3, 4, 5, 6] => [12, 15, 16];
## - [2, 3, 5, 6] => [12, 15]
## ---Разобрали на семинаре----------------------------

# count = int(input('Введите количесвто элементов списка: '))
# some_list = []

# for i in range (count):
#     number = int(input(f'Введите число: '))
#     some_list.append(number)
# new_list = []
# for i in range((count - 1) // 2 + 1):
#     number1 = some_list[i]
#     number2 = some_list[count - i -1]
#     new_list.append(number1 * number2)
# print(new_list)

## Сдано мной в ДЗ на платформе
# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

## -------------------------------------------------------------------
## № 24 - Задайте список из вещественных чисел. 
## Напишите программу, которая найдёт разницу между максимальным и 
## минимальным значением дробной части элементов.
## Пример:
##   [1.1, 1.2, 3.1, 5, 10.01] => 0.19
## -- Решение на семинаре------------

# count = int(input('Введите количесвто элементов списка: '))
# some_list = []

# for i in range (count):
#     number = input('Введите число: ')
#     some_list.append(number)

# minn = 1
# maxx = 0    
# for el in some_list:
#     if '.' in str(el):
#         dr = str(el).split('.')[1]
#         if float('0.'+ dr) > maxx:
#             maxx = float('0.'+ dr)
#         elif float('0.'+ dr) < minn:
#             minn = float('0.'+ dr)

# print(maxx - minn)

## Сдано мной ДЗ на платформе
# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

## ----------------------------------------------------------
## № 25 - Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
## Пример:
## 45 -> 101101
## 3 -> 11
## 2 -> 10
## -- Решение на семинаре---------

# a = int(input('Введите число: '))
# print(bin(a)[2: ])
## Решение алгоритмом-----

# a = int(input('Введите число: '))
# b = ''
# while a !=0:
#     b = str(a % 2) + b
#     a //= 2

# print(b)

## Сдано мной ДЗ на платформе
# s = ""
# n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

## ----------------------------------------------------------
## № 26 - Задайте число. Составить список чисел Фибоначчи, 
## в том числе для отрицательных индексов

## --- Решение на саминаре-----

# k = int(input('Введите число: '))
# some_list = [0] * (k * 2 + 1)
# some_list[k + 1] = 1
# for idx in range(k + 2, (k * 2 + 1)):
#     some_list[idx] = some_list[idx - 1] + some_list[idx - 2]
# for idx in range(k, -1, -1):
#     some_list[idx] = some_list[idx + 2] - some_list[idx + 1]

# print(some_list)

##  Сдан омной ДЗ на поатформе
# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))
## ----------------------------------------------------------
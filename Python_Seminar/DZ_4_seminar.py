## № 30. Вычислить число c заданной точностью d. 
## Пример:
## при d = 0.001, π = 3.141  10^(-1)≤d≤10^(-10)

## --- Решение на семинаре--------------

# n = float(input('Введите число: '))
# d = float(input('Введите d: '))

# if d == 1:
#     print(int(n))
# else:
#     d = str(d)
#     d = d.split('.') # Строка делится по '.' - левая часть [0], правая часть [1]
#     d = len(d[1]) # Выбираем правую сторону от точки    
#     print(round(n, d)) # round число n со знаками посля запятой длиной d

## -- Сдано мной ДЗ на платформе---
# from math import pi

# d =  int(input('Введите число для заданной точности числа Пи:\n'))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


## № 31. Задайте натуральное число N. Напишите программу, которая составит 
## список простых множителей числа N.

## --- Решение на семинаре ----------

# n = int(input('Введите число n: '))
# a = []
# for i in range(2, n + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             a.append(i)
# print(a)

## -- Сдано мной ДЗ на платформе----
# num = int(input('Введите число: '))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f'Простые множители числа {old} приведены в списке: {lst}')

## № 32. Задайте последовательность чисел. 
## Напишите программу, которая выведет список неповторяющихся 
## элементов исходной последовательности.

## - Решение на семинаре------

# a = [2 ,5, 8, 8, 3, 0, 3, 2]
# b = set(a) # Множетсво - set  - хэш таблица из уникальных элементов списка
# print(b)
# ## Можно искать в списке искомое значение
# print(3 in b) # Находится мгновенно в множестве чем просто проходиться по списку...

# a = [2 ,5, 8, 8, 3, 0, 3, 2]
# b = []
# for i in a:
#     if a.count(i) == 1:
#         b.append(i)
# print(b)

## Для ускорения можно так

# a = [2 ,5, 8, 8, 3, 0, 3, 2]
# b = []
# for i in a:
#     count = 0
#     for j in a:
#         if i  == j:
#             count += 1
#         if count == 2:
#             break
#     if count == 1:
#         print(i)
   

## -- Сдан омной ДЗ на платформе---
# lst = list(map(int, input('Введите числа через пробел:\n').split()))
# print(f'Исходный список: {lst}')
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f'Список из неповторяющихся элементов: {new_lst}')


## № 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
## (значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
## Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²

## -- Решение на семинаре----------

# import random

# some_dict = {0: '\u2070',
#            1: '\u00B9',
#            2: '\u00B2',
#            3: '\u00B3',
#            4: '\u2074',
#            5: '\u2075',
#            6: '\u2076',
#            7: '\u2077',
#            8: '\u2078',
#            9: '\u2079'}

# k = int(input('Введите натуральную степень k: '))

# coef = [random.randint(0, 100) for _ in range(k+1)]
# print(coef)
# with open('file.txt', 'w', encoding='utf-8') as m:
#     for i in range(len(coef)):
#         if k - i != 1 and k - i !=0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')

    
## -- Сдано мной ДЗ на платформе-----------
# from random import randint
# import itertools

# k = randint(2, 7)

# def get_ratios(k):
#     ratios = [randint(0, 10) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 10) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return '.join(map(str, polynomial)).replace(' 1*x',' x')


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)

# with open('Polynomial.txt', 'w') as data:
#     data.write(polynom1)


## № 35. Даны два файла, в каждом из которых находится запись многочлена. 
## Задача - сформировать файл, содержащий сумму многочленов.

# k = randint(2, 5)

# ratios = get_ratios(k) 
# polynom2 = get_polynomial(k, ratios)
# print(polynom2)

# with open('Polynomial2.txt', 'w') as data:
#     data.write(polynom2)


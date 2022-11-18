## ------------------------------------------------------
## №14 Напишите программу, которая принимает на вход вещественное число и показывает 
## сумму его цифр.
## Пример:
## - 6782 -> 23
## - 0,56 -> 11

## Решение прибавлением чисел начиная с последнего методом деления на 10 
## и взятия остатка (или целочисленного деления) - !!! не работает с дробными...!!!

# number = float(input('Введите чилсло: '))
# summ = 0

# while number != 0:
#     summ += number % 10
#     number //= 10
# print(summ)

## Решение задачи через строки

# number = input('Введите число: ')
# summ = 0
# for symbol in number:
#     if symbol != '.' and symbol != '-':
#         summ += int(symbol)
# print(summ)

## Решение через реплайс (сложный алгоритм)
# number = input('Введите число: ')
# summ = 0
# number.replace('.', '')
# number.replace('-', '')
# for symbol in number:
#     if symbol != '.' and symbol != '-':
#         summ += int(symbol)
# print(summ)

## Решение методом isdigit
# sum = 0
# input_num = input('Введите число: ')

# for a in input_num:
#     if a.isdigit():  # Проверка на является символ строки числом... И выдает True или Folse
#         sum += int(a) # Тут если True то прибавляет к sum число которое проверил isdigit

# print(sum)

##------------------------------------------------------------------
## № 15 Напишите программу, которая
## принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите чилос: '))
# some_list = [1]
# fact = 1
# for i in range(2, n+1):
#     fact *= i
#     some_list.append(fact)
# print(some_list)

## ------------
# def factorial (number, count = 1):
#     for i in range(1, number + 1):
#         count *= i
#     return count

# n = int(input('Введите число: '))
# print(f'Произведение чисел от 1 до {n} = ', end = '')
# for i in range(1, n + 1):
#     if i == n: 
#         print(f'{factorial(i)}')
#     else:
#         print(f'{factorial(i)}', end = ', ')


## № 16 Задайте список из n чисел 
## последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
## Вариант 1------
# n = int(input('Введите число: '))
# some_list = []
# for i in range (1, n+1):
#     some_list.append((1 + 1/i) ** i)
# print(sum(some_list))

## Вариант 2------
# n = int(input('Введите число: '))
# summ = 0

# for i in range(1, n+1):
#     summ += (1+1/i) ** i
# print(summ)

## Вариант переданный в ДЗ мной-----
# n = int(input('Введите число: '))

# def sequence(n):
#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print(round(sum(sequence(n))))


## 17. НЕ ОБЯЗАТЕЛЬНАЯ ЗАДАЧА
## Задайте список из N элементов, заполненных числами из промежутка [-N, N].
## Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

## Решение на семинаре------------------------

# from random import *
# n = int(input('Введите число: '))
# some_list = []
# for _ in range(n):
#     some_list.append(randint(-n, n))
# print(some_list)
# with open('file.txt', 'w', encoding = 'utf-8') as f:
#     for _ in range(randint(1, n)):
#         f.write(str(randint(0, n-1)) + '\n')
# fact = 1
# with open('file.txt', 'r', encoding = 'utf-8') as f:    
#     f = f.read().splitlines()
#     for number in f:
#          fact *= some_list[int(number)]
# print(fact)

## Решение переданное мной --------------------
# import random

# def fill_list(n: int) -> list: 
#     new_list = [random.randint(-n, n)]
#     for i in range(1, n):
#         new_list.append(random.randint(-n, n))
#         i += 1
#     return new_list

# def writing_file(k: int, n: int):
#    with open('file2_4.txt', 'w') as position:
#        for i in range(k):
#            position.write(f'{random.randint(0, n-1)}\n')

# def print_position():
#    path = 'file2_4.txt'
#    position = open(path, 'r')
#    pos_element = []
#    for line in position:
#     pos_element.append(int(line))
#    print(f'Позиции элементов: {pos_element}')
#    position.close()
#    return pos_element

# def product_elements(user_list: list, k: int) -> int:
#    path = 'file2_4.txt'
#    position = open(path, 'r')
#    product = 1
#    for line in position:
#     product = product * user_list[int(line)]
#    position.close()
#    return product

# n = int(input('Количество элементов: N = '))
# new_list = fill_list(n)
# k = int(input('Количество множителей: k = '))
# writing_file(k, n)
# print(f'Заданный список: {new_list}')
# print_position()
# print(f'Произведение элементов на заданных позициях равно {product_elements(new_list, k)}')

## № 18 Не обязательная. Реализуйте алгоритм перемешивания списка

# import random
# some_list = [1, 4, 9, 10]
# random.shuffle(some_list)
# print(some_list)

## Вариант 2 --- через алгоритм -----

# import random
# some_list = [1, 4, 9, 10]
# for _ in range(random.randint(1, 10)):
#     i1 = random.randint(0, len(some_list)-1)
#     i2 = random.randint(0, len(some_list)-1)
#     some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
# print(some_list)

## Вариант через "время" алгоритмом...--------------------

# import time
# now = time.time()
# print(now)
# random_number = str(time.time()).split('.') [1]
# some_list = [1, 4, 9, 10]
# for _ in range(int(str(time.time()).split('.')[1]) % (10 - 5 + 1) + 5):
#     i1 = int(str(time.time()).split('.')[1])  % (4-0) + 0
#     time.sleep(0.00001)
#     i2 = int(str(time.time()).split('.')[1])  % (4-0) + 0
#     some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
# print(some_list)


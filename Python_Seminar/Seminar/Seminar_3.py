###-----------------------------------------------------------
## ------------------- Задачи на Семинаре------------------------------------
## --------------------------------------------------------------------
## № 19 Реализуйте алгоритм задания случайных чисел без использования встроенного 
## генератора псевдослучайных чисел.

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
## -------------------------------------------------------------------
## № 20 Задайте список. Напишете программу, которая определит, присутсвует ли в
## заданном списк строк некое число

# a= []
# n= int(input('Введите строку: '))
# for i in range(n):
#     a.append(input())
## Или тоже самое в одну строку.............

# a = [input('Введите строку: ') for _ in range(int(input('Введите количество строк: ')))]
# find_number = input('Введите искомое число в строке: ')
# for i in a:
#     if find_number in i:
#         print('Да, искомое число есть в строках')
#         break
# else:
#     print('Нет, искомого числа в строках нет!')

##----------------------------------------------------------------------
## № 21 Напишите программу, которая определит позицию второго вхождения строки в списке либо
##сообщит, что её нет.

## Решение алгоритмом
# a = [input('Введите строку: ') for _ in range(int(input('Введите количество элементов в строке:')))]
# find_str = input('Введите искомую строку: ')

# count = 0
# for el in range(len(a)):
#     if a[el] == find_str:
#         count += 1
#     if count == 2:
#         print(el)
#         break
# else:
#     print(-1)

## С использованием метода (функции) поиск индекса--------------

# a = [input('Введите строку: ') for _ in range(int(input('Введите количество элементов в строке:')))]
# find_str = input('Введите искомую строку: ')

# first = a.index(find_str)
# second = a.index(find_str, first + 1)
# print(second)
## -------------------------------------------------------------
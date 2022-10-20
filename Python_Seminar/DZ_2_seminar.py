#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

sum = 0
input_num = input('Введите число: ')

for a in input_num:
    if a.isdigit():
        sum += int(a)

print(sum)

#Напишите программу, которая
# принимает на вход число N и выдает набор произведений чисел от 1 до N.


def factorial (number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count

n = int(input('Введите число: '))
print(f'Произведение чисел от 1 до {n} = ', end = '')
for i in range(1, n + 1):
    if i == n: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')


#Задайте список из n чисел 
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите число: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))


#4.  НЕ ОБЯЗАТЕЛЬНАЯ ЗАДАЧА
#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

def fill_list(n: int) -> list: 
    new_list = [random.randint(-n, n)]
    for i in range(1, n):
        new_list.append(random.randint(-n, n))
        i += 1
    return new_list

def writing_file(k: int, n: int):
   with open('file2_4.txt', 'w') as position:
       for i in range(k):
           position.write(f'{random.randint(0, n-1)}\n')

def print_position():
   path = 'file2_4.txt'
   position = open(path, 'r')
   pos_element = []
   for line in position:
    pos_element.append(int(line))
   print(f'Позиции элементов: {pos_element}')
   position.close()
   return pos_element

def product_elements(user_list: list, k: int) -> int:
   path = 'file2_4.txt'
   position = open(path, 'r')
   product = 1
   for line in position:
    product = product * user_list[int(line)]
   position.close()
   return product

n = int(input('Количество элементов: N = '))
new_list = fill_list(n)
k = int(input('Количество множителей: k = '))
writing_file(k, n)
print(f'Заданный список: {new_list}')
print_position()
print(f'Произведение элементов на заданных позициях равно {product_elements(new_list, k)}')




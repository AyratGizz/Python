# Задача № 27. Задайте строку из набора чисел.
# Напишите программу, которая покажет бельшее и меньшее число.
# В качестве символа - разделителя используйте пробел.

# a = list(map(int, input('Введите числа через пробел: ').split()))
# print(f'Максимальное число: {max(a)} \nМинимальное число: {min(a)}')

## Вариант от учителя----

some_str = input('Введите числа через пробел: ')
some_str = some_str.split()
maxx = int(some_str[0])
minn = int(some_str[0])
for i in some_str:
    if int(i) > maxx:
        maxx = int(i)
    elif int(i) < minn:
        minn = int(i)
print(f'Минимальное число: {minn}\nМаксимальное число: {maxx}')

# Задача № 28. Найдите корни квадратного уравнения Ax**2 + Bx + C = 0
# двумя способами:
# 1) с помощью математичсеких формул нахождения корней квадратного уравнения.
# 2) с помощью дополнительных библиотек Python

# 1)
a, b, c = map(int, input().split())

a = float(input('Введите А: '))
b = float(input('Введите B: '))
c = float(input('Введите C: '))

d = b ** 2 - 4 * a * c
if d < 0:
    print('Корней нет')
elif d == 0:
    print(-b / (2 * a))
else:
    print((-b + d ** 0.5) / (2 * a))
    print((-b - d ** 0.5) / (2 * a))

# 2) Через SymPy

from sympy import *

a = int(input('Введите А: '))
b = int(input('Введите B: '))
c = int(input('Введите C: '))
x = Symbol('x')
print(solve((a * x) ** 2 + b * x + c, x))

# Задача № 29. Задайте два числа. Напишите программу, которая найдёт НОК (
# наименьшее общее кратное) этих двух чисел

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))

for i in range(min(a, b), a * b + 1, min(a, b)):
    if i % a == 0 and i % b == 0:
        print(i)
        break


# print(sm.lcm(int(input('Введите 1 число: ')), int(input('Введите 2 число: ')))) # Решение в одну строку
# ------ Дополнительные задача -------------------------------------
# №1 Словарь - переводчик с английского на русский

def num_translate(key, dictionary):
    print(dictionary[key])


d = {'one': 'один',
     'two': 'два',
     'three': 'три',
     'four': 'четыре',
     'five': 'пыть',
     'six': 'шесть',
     'seven': 'семь',
     'eight': 'восемь',
     'nine': 'девять',
     'ten': 'десять'}
word = input('Write a word: ')
num_translate(word, d)

# №2


# №3

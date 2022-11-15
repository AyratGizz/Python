## -----Анонимные, lambda функции---------------

# def f(x):
#     return x**2

# g = f # Создана переменная которая хранит в себе ссылку на функцию 
# print (type(f))

# print (f(1))
# print (g(2))

## --------СОКРАЩАЕМ ФУНКЦИЮ------------------
# def calc1(x):
#     return x+10

# print(calc1(10))

# def calc2(x):
#     return x*10

# # print(calc2(10))

# def math (op, x):
#     print(op (x))
    
# math(calc2, 10)
# math(calc1, 10)
##-------------------------------------
# def sum (x, y):
#     return x+y

# def mylt (x, y):
#     return x*y

# def calc(op, a, b):
#    print(op(a, b))
# #    return op (a ,b)

# calc(mylt, 4, 5)

##---------- lambda---------------------

# sum = lambda x, y: x+y

# calc(sum, 4, 5)

# # или сразу в calc

# calc(lambda x, y: x+y, 5, 5)

##-----List Comprehension---------------------------------
## Для быстрого создания списков

# list = []

# for i in range(1, 101):
#     # if (i%2 ==0):
#         list.append(i)
# print(list)
## ---------Тоже самое в одной строке (без if (i%2 ==0))
# list = [i for i in range(1, 101)]
# print(list)

##-------Добавление условия 
# list = [i for i in range(1, 101) if i%2 ==0]
# print(list)

## ------------Создание пары числа (кортеж...)
# list = [(i, i) for i in range(1, 101) if i%2 ==0]
# print(list)

## Обработка данных списка 

# def f(x):
#     return x**3

# list = [f(i) for i in range(1, 101) if i%2 ==0]
# print(list)

## --------Возведение в куб в кортеже для наглядности
# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 101) if i%2 ==0]
# print(list)

##--------- С ИСПОЛЬЗОВАНИЕМ lambda------------------
# Функция которая принимает функцию и коллекцию данных
# def select(f, col):
#     return [f(x) for x in col]
## ---------Функция для Фильтрации объектов----------
# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4 5 6 7 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x:(x, x**2),res)
# print(res)

## --Тоже самое с Библиотекой Python-----
## -------------Фунция map-----------------

# li = [x for x in range (1, 21)]

# li = list(map(lambda x: x+10, li))
# print(li)

## ------При вооде данных пользователем-----

# data = list(map(int, input().split(','))) # через запятую
# print(data)

## -----Если не делать тип данных ЛИСТ а пробегаться по объектам----

# data = map(int, input().split(',')) # через запятую
# for e in data:
#     print(e)
# print('-------')

# for e in data:
#     print(e)  

##---------------------
## Функция для Фильтрации объектов
# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4 5 6 7 8 15 23 38'.split()

# res = map(int, data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x:(x, x**2),res))
# print(res)

##--------Функция ФИЛЬТР - filter--------------
## ---Тоже самое что и выше с функцией ФИЛЬТР-----
# data = [x for x in range (1, 21)]

# res = list(filter(lambda x: not x%2, data))

# print(res)

# res = map(int, data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x:(x, x**2),res))
# print(res)

## -----------------Функция ZIP------------------

# users = ['user1', 'user2', ' user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]

# data = list(zip(users, ids))
# print(data)

## -----------Функция нумерации списка ENUMERATE--------------

# users = ['user1', 'user2', ' user3', 'user4', 'user5']

# data = list(enumerate(users))
# print(data)

#------------------------------------------------------------------------

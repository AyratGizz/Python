# a - открытие для добавления данных
# r -  открытие для чтения данных
# w - открытие для записи данных (перезапись)
# w+, r+ 
#
# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line2\n')

# exit()

# colors = ['red', 'green', 'blue']
# data = open ('file.txt', 'a') # тут a это как раз мод (в данном случае добавление записи)
# data.writelines(colors) #разделителей не будет
# data.close()

# exit()

# #чтение данных из файла и вывод в консоль
# patch = 'file.txt'
# data = open(patch, 'r')
# for line in data:
#     print(line)
# data.close()


# -----Функции-----------------------------------

# def new_string (symvol, count):
#     return symvol * count
# print(new_string('!', 5))

#----передача "неограниченного" количесвтва аргументов--------------
# логика завязана для работы со строкой

# def concatenatio(*params):
#     res: str = ""  # со строкой
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# # если с числами, то будет так (Числа складываются!!!)

# def concatenatio(*params):
#     res:  int = 0
#     # res = 0    # можно не указывать тип данных
#     for item in params:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4))

# --------РЕКУРСИЯ!-------------------
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# # просмотр первых 10 чисел
# list = []
# for e in range (1, 10): 
#     list.append(fib(e))
    
# print(list) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# ----КОРТЕЖИ-----------------------
# Кортеж - это некий !Неизменяемый! "список" 

# a = (3, 4, 5)
# # print(a)
# # print(a[0])
# # print(a[-1])

# # можно  перебирать циклом фор
# for item in a:
#     print(item)

# Конвертация кортежа в переменные и работа с ними
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

#-------СЛОВАРИ----------------------------

# dictionary = {}
# # для написания ключей в столбик ( \ )
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)
# print(dictionary['left'])

# # для просмотра ключей просмотреть можно циклом
# for k in dictionary.keys():
#     print(k)

# # для просмотра значений просмотреть можно циклом
# for k in dictionary.values():
#     print(k)   


# # Чтобы присвоить новое значение по ключу

# dictionary['up'] = 'up'
# print(dictionary)


#---------МНОЖЕСТВА-----------------------------------
# colors = {'red', 'green', 'blue'}
# print(colors)

# # Добавить элемент в множество
# colors.add('gray')
# print(colors)

# # Удалить из множества
# colors.remove('red')
# print(colors)

# # Очистить множество
# colors.clear()
# print(colors)

# Работа с множеством
# a = {1, 2, 3, 4, 5}
# b = {6, 7, 8, 9, 10}
# c = a.copy() # - В данном случае в переменную с присваивается копия множества переменной а
# # Объединение множеств
# u = a.union(b)
# # Пересечение
# i = a.intersection(b)
# # 
# dl = a.difference(b)
# #
# dr = b.difference(a)
# #
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
    
# # Неизменяемое (замороженное) множество (не будет работать добавление, изменение и т.п.)

# s = frozenset(a)

#-----------СПИСКИ - РАБОТА С НИМИ-------------------------

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)
    
# print() # Вывод пустой строки

# for e in list2:
#     print(e)

# list[0] = 123

# for e in list1:
#     print(e)
    
# print() # Вывод пустой строки

# for e in list2:
#     print(e)
    
# Удаление последнего элемента списка
# print(list1)
# print(len(list1))
# print(list1.pop())
# print(list1)

# # Удаление конкретного элемента списка

# print(list1.pop(2))
# print(list1)

# # Вставка на нужную позицию элемент
# print(list1.insert(2, 11))
# print(list1)

# # Вставка элемента в конец списка
# print(list1.append(13))
# print(list1)





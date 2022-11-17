# ---------- Тип данных строка - str -----------
# friend = 'Максим'
# print(friend)
# print(type(friend))
#
# say = 'say "Hello"'
# print(say)
# say = "say 'Hello'"
# print(say)
# # ---- обращение по индексу ----
# first_letter = friend[0]
# print(first_letter)
# # ----- Срезы --------
# print(friend[1:4])
# print(friend[:4])
# print(friend[3:])
# --- Функции и метода для работы со строками ---
# len - len(friend) - длина строки (сколько в ней символов)
# find - friend.find('a') - ищем символ 'a' в строке
# split - friend.split() - разбиение строки через пробел () или символы (,), (.) и т.д.
# isdigit - friend.isdigit() -  проверка, что строка состоит только из чисел(цифр) (bool)
# upper - friend.upper() - приведение строки к "ВЕРХНЕМУ РЕГИСТРУ"
# lower - friend.lower() - приведение СТРОКИ к "нижнему регистру"
# friends = 'Максим Леонид'
# print(friends)
# print(len(friends), "- Это длина строки (количество символов в строке)")  # узнаем длину строки
# print(friends.find('Лео'), "- Это индекс вхождения Лео в строке")  # если не находит, то возвращает "-1"
# print(friends.split(), '- Это разбитый список по пробелам')
# print(friends.isdigit(), "- Означает, что в строке не найдены цифры(числа)")  # Возвращает True или False
# print(friends.upper(), '- Делает все буквы большими')
# print(friends.lower(), '- Делает все буквы маленькими')
# ------------------------ Форматирование строк --------------------------------
# name = 'Leo'
# age = 30
# hello_str = 'Привет {}, тебе {} лет!'.format(name, age)
# print(hello_str)
# ------------------------------------------------------------------------------
# ---- Деление или выборка из строк----
# top5 = 'Первые места на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
# start = top5.find('1')
# end = top5.find('4')
#
# top3 = top5[start: end]
# result = 'Поздравляем {}с успехом!'.format(top3.upper())
# print(result)
# ------------------------------------------------------------------------------
# ------ Тип данных list ------
# some_list = ['Hello', 123, True]
# print(some_list)
# print(type(some_list))
#
# empty_list = []
#
# friends = ['Max', 'Leo', 'Kate']
# print('Второй друг:', friends[1])
# len - len(friends)) - показывает длину списка
# append - friends.append('Ron') - добавляет в список Ron
# pop - friends.pop() - удаляет последний элемент списка и возвращает его (выводит в консоль)
# clear - friends.clear - очищает весь список
# remove - friends.remove('Ron') - удаление элемента из списка по его значению
# del - del friends[0] - удаление элемента из списка по индексу
# print(len(friends))
# friends.append('Ron')
# print(friends)
# print(len(friends))
# print(friends.pop())
# print(friends)
# friends.clear()
# print(friends)
# friends = ['Max', 'Leo', 'Kate']
# friends.remove('Kate')
# print(friends)
# del friends[0]
# print(friends)
# ---- Другие методы list -----
#  -- Оператор in -- результатом является bool (True, False)
# hero = 'Superman'
#
# if 'man' in hero:
#     print('Есть')
# ---- Кортеж (tuple) ----
# Список который нельзя менять
# Записывается в () круглых скобках
# -- Задача - Соревнования --
# print('Соревнования по Python')
# count = int(input('Введите количество участников: '))
# i = count
# members = []
# while i > 0:
#     name = input('Кто занял {} место: '.format(i))
#     members.append(name)
#     i -= 1
# print('В соревновании участвовали: ', sorted(members))  # sorted - сортировка по алфавиту
# members.reverse()  # Реверс списка
# result = members[:3]  # Срез - первые 3 места
# result = 'Победители: {}. Поздравляем!'.format(result)
# print(result)
# ------------------ Последовательности и цикл for in ---------------------------------------------------
# friend_name = 'Max'
# bukva_name = 'M'
# friends = ['Max', 'Leo', 'Kate']
# roles = ('admin', 'guest', 'user')
#
# if 'Max' in friends:
#     print('У меня есть друг с именем {}'.format(friend_name))
#
# if bukva_name in friend_name:
#     print('Буква {} есть в имени друга {}'.format(bukva_name, friend_name))
# # for - перебирает элементы последовательности по порядку без указания индекса
# for friend in friends:
#     print(friend)
# ------------------------------------------
# Вывод символов из имени (строки)
# for letter in friend_name:
#     print(letter)
# for role in roles:
#     print(role)
# print('------------------------------------')
# # while
# i = 0
# while i < len(friends):
#     friend = friends[i]
#     print(friend)
#     i += 1
# -----------------------------------------------------------------------------------------------------------
# ------------ Применение функции range ---------- RANGE ----------------------------------------------------
# winners = ['Max', 'Leo', 'Kate']
# numbers = range(10)
# print(list(numbers))
# for winner in winners:
#     print(winner)
# for i in range(len(winners)):
#     # print(i)
#     print(i + 1, ')', winners[i])
# numbers = [1, 2, 3]
#
# for number in numbers:
#     print(number)
#
# print(list(range(1, 1000, 2)))
#
# for number in range(1, 101, 2):
#     print(number)
# for i in range(1, lem(winners) + 1):
#     print(i, ')', winners[i-1])
# -------------------------------------------------------------------------------------------------------------
# --------------------------------- Словари -------------------------------------------------------------------
# dict - Объявляется в фигурных скобках
# friend = {
#     'name': 'Max',
#     'age': 23
# }
# print(friend)
#
# print(friend['age'])  # Получение значения по ключу
# friend['has_car'] = True  # Добавление (изменение) ключа
# del friend['age']  # Удаление и ключа и значения
# if 'age' in friend:  # Поиск ключа или элемента
#     print('Есть возраст')
# # Перебор словаря по ключам
# for key in friend.keys():
#     print(key)
#     print(friend[key])
#
# # Перебор словаря по значениям
# for val in friend.values():
#     print(val)
# # Перебор по ключам и значениям
# for item in friend.items():
#     print(item)
# # или
# for key, val in friend.items():
#     print(key)
#     print(val)
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------- МНОЖЕСТВА ------------------------------------------------------------
# set - во множестве не может быть 2 одинаковых элемента!!!!!!!
# cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
# print(type(cities))
# print(cities)
# cities = set(cities)  # Приведение к типу set (множества) где элементы не повторяются!!!
# print(cities)
# print(type(cities))
#
# cities = {'Las Vegas', 'Paris', 'Moscow'}  # Так пишутся множества
# print(cities)
# ---- Действия со множествами ----
# add - cities.add('Burma') - Добавление элемента
# remove - cities.remove('Moscow') - удаление элемента
# len - длина множества
# in, for - операторы и циклы
# работа с несколькими множествами (объединение, пересечение, и т.д....)
# cities = {'Las Vegas', 'Paris', 'Moscow'}
# print(cities)
# cities.add('Burma')
# print(cities)
# cities.remove('Moscow')
# print(cities)
# print((len(cities)))
# print('Paris' in cities)

# for city in cities:
#     print(city)
# -------------------- Операции со множествами -----------------------
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}
print(max_things | kate_things)  # | - Объединение множества
print((max_things & kate_things))  # & - Пересечение множества - Поиск повторяющихся вещей
print(max_things - kate_things)  # Что есть у Макса, чего нет у Кейт
print(kate_things - max_things)  # Что есть у Кейт чего нет у Макса
# ----------------------------------------------------------------------------------------------------------
#
#
#
# #

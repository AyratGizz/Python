# Практикум.
# Игра "Угадай число". Создание простой игры.
# Компьютер загадывает случайное число от 1 до 100. Пользователь должен его угадать.
# Если пользователь не угадал, программа дает подсказку: введенное число больше или меньше...
# import random
#
# print('Компьютер загадал число от 1 до 100, попробуйте его отгадать!')
# number = random.randint(1, 100)
# # print(number)
#
# while True:
#     user_number = int(input('Введите число: '))
#     # print('Вы ввели число -', user_number)
#     if number == user_number:
#         print('Вы угадали!')
#         break
#     elif number < user_number:
#         print('Ваше число больше загаданного!')
#     else:
#         print('Ваше число меньше загаданного!')
# Добавить в игру уровни сложности. Чем сложнее, тем меньше попыток на то, чтобы угадать число.
import random

user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя {i + 1} игрока: ')
    users.append(user_name)
print('------------------------------------------')
print(f'Приступим к Игре {users}', sep=',')
print('-> Компьютер загадал число от 1 до 100, попробуйте его отгадать!')
number = random.randint(1, 100)
# print(number)  # Вывод загаданного случайного числа
user_number = None
count = 0
levels = {1: 15, 2: 10, 3: 5}
print('-> Есть 3 уровня сложности:')
print('     Уровень 1: Количество попыток - 15')
print('     Уровень 2: Количество попыток - 10')
print('     Уровень 3: Количество попыток - 5')
level = int(input('Введите желаемый уровень сложности - 1, 2 или 3: '))
max_count = levels[level]

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print(f'Превышен лимит попыток ({max_count}). Все игроки проиграли!')
        break
    print(f'Попытка № {count}', end=' - ')
    for user in users:
        print(f'Ход игрока {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного!')
        else:
            print('Ваше число меньше загаданного!')
else:
    print(f'!!! УРРРАААА !!! {winner_name} угадал число - {number} и ПОБЕДИЛ!')

#
#
#
# #

## Задача нахождения максимума
# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))

# print('a =', a)
# print('b =', b)

# c = a * b
# print('с = a * b =', a * b)
# c = int(c)

# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c

# print(f'Максимальное число = {max}')

# # Задача про школу (Кахут)

# prazdnik = True
# temperature_limit = int(input('Введите минимально допустимую температуру:'))
# temperature = int(input('Введите температуру на улице: '))
# age_limit = int(input('Введите максимальный возраст младших классов:'))
# age = int(input('Введите ваш возраст: '))


# if prazdnik == True:
#     print('Идем к друзьям!')
# elif temperature < temperature_limit:
#     print('Идём в школу!')
# elif age < age_limit:
#     print('Сидим дома!')
# else:
#     print('Сегодня учебный день!')

## Задача друзья с собакой    

# first_friend_speed = 4
# second_friend_speed = 5
# dog_speed = 10
# distance = 1000
# distance_limit = 1
# dog_counter = 0
# dog_direction = 1
# while distance > distance_limit:
#     speed = 0
#     if dog_direction == 1:
#         speed = first_friend_speed + dog_speed
#         dog_direction = 2
#     else:
#         speed = second_friend_speed + dog_speed
#         dog_direction = 1
#     time_to_meet = distance / speed
#     distance = distance - (time_to_meet * (first_friend_speed + second_friend_speed))
#     dog_counter += 1
#     print(f'Дистанция которую пробежала собака: {distance}')
# print(f'Собака пробежала от одного друга к другому {dog_counter} раз')


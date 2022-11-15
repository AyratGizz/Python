import random
# import tkinter # Обертка (графика)
# import wxPython # Обертка (графика)
user_name = input('Введите ваше имя: ')
print(f'Привет {user_name}! \nДавай сыграем в игру отгадай слово "Поле Чудес"!')
print('Допускается сделать 10 ошибок!')
words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека', 'шайба', 'олимпиада']

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
# print(*gamer_word)
print(f'Нужно отгадать слово из "{len(secret_word)}" букв')
print(''.join(gamer_word))

errors_cnt = 0
while True:
    letter = input('Введите одну русскую букву: ')
    # Валидация по длине символа: ord(letter) -> int; || re -> pattern
    if len(letter) != 1:
        continue
    if letter in secret_word:
        # idx = 0
        # for symbol in secret_word:
        #     if symbol == letter:
        #         gamer_word[idx] = letter
        #     idx += 1
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[idx] = letter
        if '*' not in gamer_word:
            print('Вы выиграли!!!')
            break
    else:
        errors_cnt += 1
        print('Допущено ошибок:', errors_cnt)
        if errors_cnt == 10:
            print('Вы проиграли!')
            break
    print(''.join(gamer_word))
print('Сыграйте ещё!!!')
from datetime import datetime
from controller import *


def write(func, data=None):
    operation = {1: '"Добавление сотрудника"', 2: '"Вывод списка всех сотрудников"', 3: '"Поиск сотрудника"',
                 4: '"Удаление сотрудника из базы"', 5: '"Завершение работы"'}
    with open('log_cash.txt', 'a', encoding='utf-8') as l:
        if func == 1:
            result = 'Выполняемая операция - {}. Информация - {}. Время выполнения - {}'.format(operation[func],
                                                                                                data, datetime.now())
        elif func == 3:
            result = 'Выполняемая операция - {}. Информация - {}. Время выполнения - {}'.format(operation[func],
                                                                                                data, datetime.now())
        elif func == 4:
            result = 'Выполняемая операция - {}. Информация - {}. Время выполнения - {}'.format(operation[func],
                                                                                                data, datetime.now())
        else:
            result = 'Выполняемая операция - {}. Время выполнения - {}'.format(operation[func], datetime.now())
        l.write(f'{result}' + '\n')

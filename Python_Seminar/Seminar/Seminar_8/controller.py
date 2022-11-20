# Создать информационную систему, позволяющую работать с сотрудниками
# некой компании \ студентами вуза \ учениками школы
# #
from operation import *
from view import *
from log import *


def button_click():
    func = ''
    while func != 5:
        func = int(input('Для добавления сотрудника введите - 1, \n'
                         'Для вывода списка всех сотрудников введите - 2, \n'
                         'Для поиска сотрудника введите - 3, \n'
                         'Для удаления работника из базы введите - 4 , \n'
                         'Для завершения работы программы введите - 5, \n'
                         'Введите здесь: '))
        if func == 1:
            result = fio()
            record_data(result)
            write(func, result)
        if func == 2:
            reading_reference()
            write(func)
        if func == 3:
            poisk = input('Кого ищем? : ')
            search_subscriber(poisk)
            write(func, poisk)
        if func == 4:
            delete_job = input('Кого удалить из базы?: ')
            delete_subscriber(delete_job)
            write(func, delete_job)
    print('Такой функции нет!!! Выберите функцию от 1 до 5!!!')

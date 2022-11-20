# Создать информационную систему, позволяющую работать с сотрудниками
# некой компании \ студентами вуза \ учениками школы
# #
from operation import *
from view import *
from log import *
from operation import field_names


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
            field_names()
            # file_exists = os.path.isfile('reference.csv')
            # with open('reference.csv', 'a', newline='', encoding='utf-8') as f:
            #     fieldnames = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Возраст', 'Должность', 'Телефон']
            #     writer = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames)
            #     if not file_exists:
            #         writer.writeheader()
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

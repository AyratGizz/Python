import csv
import os.path
from view import *


def record_data(dictt):
    file_exists = os.path.isfile('reference.csv')
    with open('reference.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['ID', 'Имя', 'Фамилия', 'Отчество', 'Возраст', 'Должность', 'Телефон']
        writer = csv.DictWriter(f, delimiter=';', fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(dictt)
    view_data('Данные записаны успешно.\n')


def reading_reference():
    try:
        with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                view_data('ID: {}, '
                          'Имя: {}, '
                          'Фамилия: {},  '
                          'Отчество: {}, '
                          'Возраст {}, '
                          'Должность {}, '
                          'Телефон: {}'.format(row['ID'],
                                               row['Имя'],
                                               row['Фамилия'],
                                               row['Отчество'],
                                               row['Возраст'],
                                               row['Должность'],
                                               row['Телефон']))
    except:
        view_data('База данных отсутствует!\n')


def search_subscriber(strr):
    try:
        with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            flag = False
            for row in reader:
                if strr in row.values():
                    view_data('Результат поиска:\n {}\n'.format(row))
                    flag = True
            if flag == False:
                view_data('Такого сотрудника в базе нет.')
    except:
        view_data('База данных отсутствует!\n')

# def delete_subscriber(strr):
#     try:
#         with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
#             reader = csv.DictReader(f, delimiter=';')
#             flag = False
#             for row in reader:
#                 if strr in row.values():
#                     view_data('Результат поиска:\n {}\n'.format(row))
#                     flag = True
#             if flag == False:
#                 view_data('Такого сотрудника в базе нет.')
#     except:
#         view_data('База данных отсутствует!\n')

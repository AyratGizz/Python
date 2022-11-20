# import pandas as pd
# from csv import *


def view_data(data):
    print(f'{data}')


# row_count = pd.read_csv("reference.csv")
# rowcount = len(row_count)


# rowcount = None
#     for row in open("reference.csv"):
#         rowcount += 1

def fio():
    # global rowcount
    # try:
    #     row_count = 0
    #     with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
    #         reader = csv.DictReader(f, delimiter=';')
    #         for row in open("reference.csv"):
    #             rowcount += 1
    # except:
    #     print('База данных пуста!')
    # user_id = rowcount + 1
    user_id = 1
    sur_name = input('Введите Фамилию работника: ')
    name = input('Введите Имя работника: ')
    patronymic = input('Введите Отчество работника: ')
    age = int(input('Введите Возраст работника: '))
    job_title = input('Введите Должность работника: ')
    phone = int(input('Введи Номер телефона работника:'))
    data = {'ID': user_id, 'Фамилия': sur_name, 'Имя': name, 'Отчество': patronymic,
            'Возраст': age, 'Должность': job_title, 'Телефон': str(phone)}
    return data

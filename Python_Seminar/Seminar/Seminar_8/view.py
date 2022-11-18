import csv
import pandas as pd


def view_data(data):
    print(f'{data}')


row_count = pd.read_csv("reference.csv")
rowcount = len(row_count)


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
    user_id = rowcount + 1
    name = input('Введите Имя работника: ')
    sur_name = input('Введите Фамилию работника: ')
    patronymic = input('Введите Отчество работника: ')
    age = int(input('Введите Возраст работника: '))
    dolznost = input('Введите Должность работника: ')
    phone = int(input('Введи Номер телефона работника:'))
    data = {'ID': user_id, 'Имя': name, 'Фамилия': sur_name, 'Отчество': patronymic,
            'Возраст': age, 'Должность': dolznost, 'Телефон': str(phone)}
    return data

import csv
import os
import pandas as pd


def view_data(data):
    print(f'{data}')


def fio():
    row_count = pd.read_csv("reference.csv")
    rowcount = len(row_count)
    user_id = rowcount + 1
    sur_name = input('Введите Фамилию работника: ')
    name = input('Введите Имя работника: ')
    patronymic = input('Введите Отчество работника: ')
    age = int(input('Введите Возраст работника: '))
    job_title = input('Введите Должность работника: ')
    phone = int(input('Введи Номер телефона работника:'))
    data = {'ID': user_id, 'Фамилия': sur_name, 'Имя': name, 'Отчество': patronymic,
            'Возраст': age, 'Должность': job_title, 'Телефон': str(phone)}
    return data
    # print('База данных пуста!')

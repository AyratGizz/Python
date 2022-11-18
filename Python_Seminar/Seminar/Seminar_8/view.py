import csv


def view_data(data):
    print(f'{data}')


def fio():
    # try:
    #     with open('reference.csv', 'r', newline='', encoding='utf-8') as f:
    #         reader = csv.DictReader(f, delimiter=';')
    #         row_count = sum (1 for row in reference.csv)
    #
    # except:

    name = input('Введите Имя работника: ')
    sur_name = input('Введите Фамилию работника: ')
    patronymic = input('Введите Отчество работника: ')
    age = int(input('Введите Возраст работника: '))
    dolznost = input('Введите Должность работника: ')
    phone = int(input('Введи Номер телефона работника:'))
    data = {'Имя': name, 'Фамилия': sur_name, 'Отчество': patronymic,
            'Возраст': age, 'Должность': dolznost, 'Телефон': str(phone)}
    return data

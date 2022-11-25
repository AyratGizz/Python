# class Selector:
#     def __init__(self, a):
#         self.selector = a
#         self.evens = []
#         self.odds = []
#         for i in self.selector:
#             if i % 2 != 0:
#                 self.odds.append(i)
#             else:
#                 self.evens.append(i)
#
#     def get_odds(self):
#         return self.odds
#
#     def get_evens(self):
#         return self.evens
#
#
# values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
# selector = Selector(values)
# odds = selector.get_odds()
# evens = selector.get_evens()
# print(' '.join(map(str, odds)))
# print(' '.join(map(str, evens)))

# --- Задача 2 ---

# class AmericanDate:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def get_year(self):
#         self.year = str(self.year)
#         return self.year
#
#     def get_month(self):
#         self.month = str(self.month).zfill(2)
#         return self.month
#
#     def get_day(self):
#         self.day = str(self.day).zfill(2)
#         return self.day
#
#     def format(self):
#         # if len(self.get_day()) > 1 and len(self.get_month())> 1:
#         #     return f'{self.get_month()}.{self.get_day()}.{self.get_year()}'
#         # if len(self.get_day()) == 1 and len(self.get_month()) ==1:
#         #     return f'0{self.get_month()}.0{self.get_day()}.{self.get_year()}'
#         # if len(self.get_day())> 1 and len(self.get_month())
#         return '{:02}.{:02}.{:04}'.format(self.month, self.day, self.year)
#
#     def set_year(self, y):
#         self.year = y
#
#     def set_month(self, m):
#         self.month = m
#
#     def set_day(self, d):
#         self.day = d
#
#
# class EuropeanDate:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def get_year(self):
#         self.year = str(self.year)
#         return self.year
#
#     def get_month(self):
#         self.month = str(self.month)  # .zfill(2)
#         return self.month
#
#     def get_day(self):
#         self.day = str(self.day)  # .zfill(2)
#         return self.day
#
#     def format(self):
#         return '{:02}.{:02}.{:04}'.format(self.day, self.month, self.year)
#
#     ###
#     def set_year(self, y):
#         self.year = y
#
#     def set_month(self, m):
#         self.month = m
#
#     def set_day(self, d):
#         self.day = d
#
#
# american = AmericanDate(2000, 4, 10)
# american.set_month(2)
# european = EuropeanDate(2000, 4, 10)
# european.set_month(2)
# print(american.format())
# print(european.format())


# --- Задача 3 ---

class Person:

    def __init__(self, name, surname, oth, numbook):
        self.name = name
        self.oth = oth
        self.surname = surname
        self.numbook = numbook

    def get_phone(self, key='private'):
        return self.numbook.get(key)

    def get_name(self):
        return f'{self.surname} {self.name} {self.oth}'

    def get_work_phone(self):
        return self.get_phone('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.oth}\n' \
               f'Примите участие в нашем беспроигрышном конкурсе для физических лиц'


class Company:

    def __init__(self, name, type_, numbook, *arg):
        self.name = name
        self.type_ = type_
        self.numbook = numbook
        self.person = arg

    def get_phone(self, key='contact'):
        if key in self.numbook:
            return self.numbook.get(key)
        for person in self.person:
            number = person.get_work_phone()
            if number:
                return number

    def get_name(self):
        return f'{self.name}'

    def get_work_phone(self):
        return self.get_phone()

    def get_sms_text(self):
        return f'Для компании {self.name} есть супер предложение! \
Примите участие в нашем беспроигрышном конкурсе для {self.type_}'


def send_sms(*obj):
    for ob in obj:
        number = ob.get_phone()
        if number:
            print(f'Отправлено СМС на номер {number} \
с текстом: {ob.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {ob.get_name()}')


if __name__ == '__main__':
    print('TEST 1  ___________________')
    person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
    person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
    person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
    person4 = Person("John", "Unknown", "Doe", {})
    company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
    company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
    company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)
    print('TEST 2  ___________________')
    person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
    person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
    person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
    person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
    company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
    company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
    company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
    send_sms(person1, person2, person3, person4, company1, company2, company3)

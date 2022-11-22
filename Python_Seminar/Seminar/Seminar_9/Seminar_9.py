# class Auto:
#     # атрибуты класса
#     auto_count = 0
#
#     # инициализатор (магический метод)
#     def __init__(self, auto_name, auto_model, auto_year):
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#
#     # метод класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print('Автомобиль заведен')
#         # если создать инициализатор, то ниже можно не писать
#         # self.auto_name = auto_name
#         # self.auto_model = auto_model
#         # self.auto_year = auto_year
#
#
# # объект
# a = Auto('Audi', 'A4', 2015)
# # a.on_auto_start('Audi', 'A4', 2015)
# print(Auto.auto_count)
#
# print(a.auto_name)
# print(a.auto_model)
# print(a.auto_year)
# ---------- Задача 1 ------------------

# class LittleBell:
#     def sound(self):
#         print('ding')
#
#
# bell = LittleBell()
# bell.sound()
# bell.sound()
# bell.sound()


# ---------- Задача 2 ------------------

# class Button:
#     count = 0
#
#     def click(self):
#         Button.count = + 1
#
#     def click_count(self):
#         return Button.count
#
#     def reset(self):
#         Button.count = 0
#
#
# button = Button()
# button.click()
# button.click()
# button.click()
# print(button.click_count())
# button.click()
# print(button.click_count())
# button.reset()
# print(button.click_count())


# ---------- Задача 3 ------------------


# class Balance:
#     def __init__(self):
#         self.add_left_count = 0
#         self.add_right_count = 0
#
#     def add_right(self, ves):
#         self.add_right_count += ves
#
#     def add_left(self, ves):
#         self.add_left_count += ves
#
#     def result(self):
#         if self.add_right_count > self.add_left_count:
#             return 'R'
#         elif self.add_right_count < self.add_left_count:
#             return 'L'
#         else:
#             return '='
#
#
# balance = Balance()
#
# # balance.add_right(10)
# # balance.add_left(9)
# # balance.add_left(2)
# # print(balance.result())
#
# balance.add_right(10)
# balance.add_left(5)
# balance.add_left(5)
# print(balance.result())
# balance.add_left(1)
# print(balance.result())

# ---------- Задача 4 ------------------

# class BigBell:
#     def __init__(self):
#         self.count = 0
#
#     def sound(self):
#         if self.count == 0:
#             print('Ding')
#             self.count += 1
#         else:
#             print('Dong')
#             self.count -= 1
#
#
# bell = BigBell()
# bell.sound()
# bell.sound()
# bell.sound()

# ---------- Задача 5 ------------------

# class Odd_even_separator:
#     even_list = []
#     odd_list = []
#
#     def add_number(self, number):
#         if number % 2 == 0:
#             self.even_list.append(number)
#         else:
#             self.odd_list.append(number)
#
#     def even(self):
#         return self.even_list
#
#     def odd(self):
#         return self.odd_list
#
#
# separartor = Odd_even_separator()
# separartor.add_number(1)
# separartor.add_number(5)
# separartor.add_number(6)
# separartor.add_number(8)
# separartor.add_number(3)
# print(' '.join(map(str, separartor.even())))
# print(' '.join(map(str, separartor.odd())))

# ---------- Задача 6 ------------------

# class MinMaxWordFinder:
#     def __init__(self):
#         self.text_list = []
#         self.min_list = []
#         self.max_list = []
#         self.len_string = 0
#
#     def add_sentence(self, string):
#         string = string.split(' ')
#         self.text_list.extend(string)
#         # for i in range(len(string) - 1):
#         #     if len(string[i]) >= len(string[i + 1]):
#         #         self.max_list.append(string[i])
#         #     elif len(string[i]) <= len(string[i + 1]):
#         #         self.min_list.append(string[i])
#
#     def shortest_words(self):
#         return sorted(self.min_list)
#
#     def longest_words(self):
#         return sorted(self.max_list)
#
#
# finder = MinMaxWordFinder()
# finder.add_sentence('hello abc world')
# finder.add_sentence('def asdf qwert')
# print(' '.join(finder.shortest_words()))
# print(' '.join(finder.longest_words()))

# --- Решение учителя ---

class MinMaxWordFinder:
    def __init__(self):
        self.text_list = []

    def add_sentence(self, sentence):
        words = sentence.split()
        self.text_list.extend(words)

    def shortest_words(self):
        minn = self.text_list[0]
        for word in self.text_list:
            if len(word) < len(minn):
                minn = word
        # short_list = []
        # for word in self.text_list:
        #     if len(word) == len(minn):
        #         short_list.append(word)
        short_list = list(filter(lambda x: len(x) == len(minn), self.text_list))
        return sorted(short_list)

    def longest_words(self):
        maxx = self.text_list[0]
        for word in self.text_list:
            if len(word) > len(maxx):
                maxx = word
        short_list = list(filter(lambda x: len(x) == len(maxx), self.text_list))
        return sorted(list(set(short_list)))


a = MinMaxWordFinder()
a.add_sentence('abc abc ds')
a.add_sentence('sd fd fd nba')
print(a.shortest_words())
print(a.longest_words())

# class Car:
#     def __init__(self, color, year, max_speed):
#         self.color = color
#         self.year = year
#         self.max_speed = max_speed
#
#     def __add__(self, other):
#         return self.max_speed + other.max_speed
#
#
# bmw = Car('black', 2018, 250)
# audi = Car('yellow', 2016, 240)
# print(bmw + audi)
# print(bmw.__add__(audi))  # Аналогия верхнего принта


# class Car:
#     def __init__(self, max_speed):
#         self.max_speed = max_speed
#
#     def __add__(self, other):
#         return Car(self.max_speed + other.max_speed)
#
#     def __str__(self):
#         return str(self.max_speed)
#
#
# bmw = Car(250)
# audi = Car(240)
# moskvich = Car(500)
# volvo = Car(700)
# print(bmw + audi + moskvich + volvo)
# # print(bmw.__add__(audi))  # Аналогия верхнего принта
# ------------------------------
# class ReversedList:
#
#     def __init__(self, somelist):
#         self.somelist = list(reversed(somelist)) #  или так  = somelist[::-1]
#
#     def __getitem__(self, item):
#         return self.somelist[item]
#
#     def __len__(self):
#         return len(self.somelist)
#
#
# rl = ReversedList([10, 20, 30])
# for i in range(len(rl)):
#     print(rl[i])
# --------------------------------

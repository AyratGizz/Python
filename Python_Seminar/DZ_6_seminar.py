## Дан список:
## ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
## Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и 
## кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:'''

# list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# lenght: int = len(list1)
# store_id = id(list1)
# for i in range(lenght):
#     entity = list1.pop(0)
#     if  entity.isdigit():
#         list1.append(F'"{int(entity):02d}"')
#     elif entity[0] == "+" and entity[1].isdigit():
#         list1.append(F'"+{int(entity):02d}"')
#     else:
#         list1.append(entity)
# print(' '.join(list1))

## Дан список, содержащий искажённые данные с должностями и именами сотрудников:
## ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
## Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 
## 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести 
##их к корректному виду. Можно ли при этом не создавать новый список?'''

# text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
#            'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# hi = 'Привет, {}!'

# for new_text in text:
#     print(hi.format(new_text.split()[-1].title()))

# ## Создать список, содержащий цены на товары (10–20 товаров), например:
# ## [57.8, 46.51, 97, ...]
# ## Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# ## Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# ## Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# ## Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

# list = [57.8, 46.51, 97, 66, 19.48, 83, 33.11, 55, 7.77, 49]

# store_id = id(list)
# print(f"{'Цена с обозначением руб, коп':-^60}")
# end_word: str = ", "

# for i, num in enumerate(list):

#     fix_price = str(f"{float(num):.2f}").split(".")

#     if i == len(list) - 1:
#         end_word = "\n"

#     print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)


# print(f"{'Сортировка цен по возрастанию':-^60}")
# print(f"id перед сортировкой {store_id}")
# list.sort()
# print(list)
# print(f"id после сортировки {id(list)}")

# print(f"{'Сортировка цен по убыванию':-^60}")

# copy_of_list = list.copy()
# copy_of_list.sort(reverse=True)

# print(copy_of_list)
# print(store_id)
# print(id(copy_of_list))


# print(f"{'Цены пяти самых дорогих товаров':-^60}")
# print(list[-6:-1])
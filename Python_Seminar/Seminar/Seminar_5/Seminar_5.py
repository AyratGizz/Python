# № 35. В файле находится N натуральных чисел, записанны через пробел. Среди чисел
# не хватает одного, чтобы выполнялось условие A[i] -1 = A[i-1]. Найдите это число

# --Решение учителя

n = 8
with open('text.txt', 'r', encoding='utf-8') as k:
    some_list = list(map(int, k.readline().split(',')))
    for i in range(n - 1):
        if some_list[i] != some_list[i + 1] - 1:
            print(some_list[i + 1] - 1)

# -- Решение в группе ----
with open('text.txt', 'r', encoding='utf-8') as f:
    s = f.readline().split(',')
    print(len(s))
    print(s)
for i in range(len(s) - 1):
    if int(s[i]) + 1 != int(s[i + 1]):
        print(int(s[i]) + 1)

# ------------------------------------------------------------------------
# Дан список интов, повторяющихся элементов в списке нет. Нужно
# преобразовать это множество в строку, сворачивая соседние по числовому ряду
# числа в диапазоны.
# Примеры:
# [1, 4, 5, 2, 3, 9, 8, 11, 0] => "0-5, 8-9, 11"
# [1, 4, 3, 2] => "1-4"
# [1, 4] => "1, 4"

int_list = [1, 4, 5, 2, 3, 9, 8, 11, 0]
int_list.sort()  ## Сортировка от минимума к максимуму
idx = 0
new_list = []
while idx < len(int_list):
    some_list = [int_list[idx]]
    new_idx = idx
    while new_idx + 1 != len(int_list) and int_list[new_idx] == int_list[new_idx + 1] - 1:
        some_list.append(int_list[new_idx + 1])
        new_idx += 1
    new_list.append(some_list)
    idx += len(some_list)
print(new_list)

a = []
for i in new_list:
    if len(i) != 1:
        a.append(f'{i[0]}-{i[-1]}')
    else:
        a.append(f'{i[0]}')
print(*a, sep=',')  # распаковка списка с добавлением  заяптой между ними.

# -------------------------------------------------------------------------
# № 36. Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2,3] или [1,7] или [1, 6, 7]  и т.д.

# -------------------------------------------------------------------------
# № 38. Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = input('Введите текст: ')
text = text.split()
new_text = ''
for i in text:
    if 'абв' not in i:
        new_text += i + ' '
print(new_text)

# С применением фильтра-----------

text = input('Введите текст: ')
text = text.split()
new_text = list(filter(lambda x: 'абв' not in x, text))
print(new_text)


## Вариант если функцию  фильтра напишем сами...-------------
def x(i):
    return 'абв' not in i


text = input('Введите текст: ')
text = text.split()
new_text = list(filter(x, text))
print(new_text)

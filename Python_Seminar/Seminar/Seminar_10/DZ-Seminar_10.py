# Задача 1.----------------------------------------------------------------------------
# Пример 1.-------------------------------
# values = [1, 2, 4, 5]
#
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
#
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
#
# Пример 2.----------------------
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
#
# print(mins.result(), maxs.result(), average.result())
#
# Пример 3.--------------
# values = [1, 0, 0]
#
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
#
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
#
#
#
# ### ------------------------------------------------------------------------------------
# Задача 2.
# Пример 1.
# tab = Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(1)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# Пример 2.
# tab = Table(2, 2)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 20)
# tab.set_value(1, 0, 30)
# tab.set_value(1, 1, 40)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(0)
# tab.add_col(1)
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# Пример 3.
# tab = Table(1, 1)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.set_value(0, 0, 1000)
#
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()
#
# tab.add_row(0)
# tab.add_row(2)
# tab.add_col(0)
# tab.add_col(2)
#
# tab.set_value(0, 0, 2000)
# tab.set_value(0, 2, 3000)
# tab.set_value(2, 0, 4000)
# tab.set_value(2, 2, 5000)
#
# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

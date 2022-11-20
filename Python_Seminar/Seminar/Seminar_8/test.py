import csv
from csv import writer
import pandas as pd

row_count = pd.read_csv("reference.csv")
rowcount = len(row_count)

print(rowcount)

# # result_count_delete = 0
# with open('reference.csv', 'r+', encoding='utf-8') as d:
#     read_2 = d.readlines()
#     d.seek(0)
#     for line in read_2:
#         if "6756658999999" not in line:
#             d.write(line)
#         d.truncate()
#
# # with open('reference.csv', 'w', encoding='utf-8') as d:
# #     writer = csv.writer(d, delimiter=' ')
# #     writer.writerow(read_2)

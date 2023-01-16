# В файле file.csv содержится табличка с полями id, name, age.
# В качестве разделителя используется: ','
# Рассчитайте медиану по возрасту людей (поле age) в таблице и запишите значение в переменную ans.

import csv
import statistics

with open('file.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    ages = []
    for row in reader:
        ages.append(int(row['age']))
ans = statistics.median(ages)

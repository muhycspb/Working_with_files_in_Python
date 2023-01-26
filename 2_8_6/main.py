# Посчитайте количество различных значений в key-value хранилище shelve users. Ответ запишите в переменную answer.

import shelve

with shelve.open('users') as file:
    answer = len(set(value for value in file.values()))
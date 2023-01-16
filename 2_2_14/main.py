# В файле in.txt записан текст. Проведите его нормализацию при помощи алгоритма NFKD.
# Результат запишите в переменную ans.

import unicodedata

with open('in.txt') as file:
    ans = unicodedata.normalize('NFKD', file.read())

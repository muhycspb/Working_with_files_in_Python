# Прочитайте текст из файла file.txt. Найдите в тексте слово, которое повторяется чаще всего.
# Запишите в переменную word само слово и в переменную word_count количество его повторений.
# В тексте в качестве разделителей используются пробел, точка и запятая.
# Печатать в консоль ничего не нужно.

from collections import Counter

with open('file.txt', encoding='utf8') as file:
    text = (i if i not in '!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~' else ' ' for i in file.read())
    text = ''.join(text).split()
    most_common = Counter(text).most_common(1)
    word, word_count = most_common[0][0], most_common[0][1]

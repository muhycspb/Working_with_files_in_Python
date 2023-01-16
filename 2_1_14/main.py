# Прочитайте файл ex.txt , записанный в кодировке UTF-16 и запишите
# содержащуюся в нем информацию в переменную answer.
# Затем дополните файл ex.txt новой строкой hacked.

with open('ex.txt', encoding='utf-16') as file:
    answer = file.read()

with open('ex.txt', 'rtb', encoding='utf-16') as file:
    file.write('\nhacked')

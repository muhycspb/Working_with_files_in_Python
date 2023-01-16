# Дан файл file.txt. Замените в его содержимом первые 6 символов на их ASCII коды.
# Пример:
# Исходная строка: hello my friend
# Результат: 10410110810811132my friend

with open('file.txt', 'r+', encoding='utf-8') as file:
    text = ''.join([str(ord(i)) for i in file.read(6)])
    text += file.read()
    file.seek(0)
    file.write(text)

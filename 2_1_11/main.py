# Проверьте существование файла data.txt.
# Если файл существует – создайте новый файл out.txt и запишите в него содержимое файла data.txt.
# Если не существует, создайте файл data.txt со строкой Третий фактор.

try:
    with open('data.txt', 'x', encoding='utf-8') as file:
        file.write('Третий фактор')

except FileExistsError:
    with open('data.txt', encoding='utf-8') as file_in:
        with open('out.txt', 'w', encoding='utf-8') as file_out:
            file_out.write(file_in.read())

# Напишите программу, которая посимвольно скопирует содержимое файла in.txt в файл out.txt.
# За раз нужно считывать символов столько, чтобы оперативная память не страдала, к примеру 65536.

BLOCK_SIZE = 65536

with open('in.txt', encoding='utf-8') as file_in, open('out.txt', 'a', encoding='utf-8') as file_out:
    while data := file_in.read(BLOCK_SIZE):
        file_out.write(data)
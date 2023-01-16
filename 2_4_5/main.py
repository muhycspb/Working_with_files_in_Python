# Напишите программу, которая достанет содержимое в кодировке cp1252 из
# бинарного файла file.bin и запишет результат в result.txt в кодировке UTF-16.

with open('file.bin', 'rb') as file, open('result.txt', 'w', encoding='UTF-16') as result:
    result.write(file.read().decode("cp1252"))

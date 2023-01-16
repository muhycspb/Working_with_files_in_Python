# Напишите программу, которая создает в текущей директории папку files
# и в ней текстовый файл file.txt, содержащий текст text of the file.
# В качестве переменной для файла используйте имя f.

import os

os.mkdir('files')

with open('files/file.txt', 'w') as f:
    f.write('text of the file')

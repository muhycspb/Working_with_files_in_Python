# Вам дан бинарный файл file.bin, который содержит пакет данных. Структура пакета следующая:
# сначала идет длина пакета – unsigned int
# затем ID пакета (не входит в длину пакета)  – unsigned short
# Содержимое пакета char[]
# Ваша задача – записать в переменную ans_id ID пакета, а в переменную ans_data его содержимое.

import struct

with open('file.bin', 'rb') as file:
    len_data = struct.unpack('I', file.read(4))[0]
    data = file.read()
    ans_id, ans_data = struct.unpack(f'H{len_data}s', data)

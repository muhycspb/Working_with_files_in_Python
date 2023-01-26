# Напишите программу, которая считывает файл file.pickle. Не забудьте, что в файле может содержаться
# вредоносный код, поэтому вы перед считыванием содержимого обязательно должны проверить сигнатуру файла.
# Ключ и сигнатура хранятся в файле secrets.txt в разных строках.
# В случае если сигнатура верная – достаньте из файла file.pickle словарь и добавьте в него новый ключ
# answer со значением easy pickle.
# Если же сигнатура неверная – создайте новый словарь к ключом answer и значением not correct.
# Полученный словарь запишите в файл answer.json.
# Создайте в отдельной папке файл file.pickle. Лучше при помощи программы.
# Создайте в этой же папке файл secrets.txt.
# Запишите туда ключ и сигнатуру с которой будете делать сравнение. Сигнатуру тоже нужно выпустить самому.
import pickle
import json
import hmac
import hashlib

with open('file.pickle', 'rb+') as pickle_file, open('secrets.txt', 'r') as secrets_file, open('answer.json', 'w') as json_file:
    SECRET_KEY = secrets_file.readline().strip()
    SIGNATURE = secrets_file.readline().strip()
    digest = hmac.new(SECRET_KEY.encode(), pickle_file.read(), hashlib.sha256).hexdigest()
    if digest == SIGNATURE:
        pickle_file.seek(0)
        data = pickle.load(pickle_file)
        print(type(data), data)
        unpickled = pickle.loads(data)
        print(type(unpickled), unpickled)
        unpickled['answer'] = 'easy pickle'
        print(type(unpickled), unpickled)
        json.dump(unpickled, json_file)
    else:
        json.dump({'answer': 'not correct'}, json_file)
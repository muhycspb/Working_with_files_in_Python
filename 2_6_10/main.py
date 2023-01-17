# Вам дана конфигурация из популярной библиотеки Poetry, достаньте из нее метадату:
# version – версию проекта
# name – Название проекта
# authors – Список авторов.
# Прочитайте файл с именем pyproject.toml.
# Сохраните результаты в виде объекта JSON с теми же ключами и положите в файл result.json.

import tomllib
import json

with open('pyproject.toml', 'rb') as toml_file, open('result.json', 'w') as json_file:
    data = tomllib.load(toml_file)['tool']['poetry']
    data = dict(zip(['version', 'name', 'authors'], [data['version'], data['name'], data['authors']]))
    json.dump(data, json_file)
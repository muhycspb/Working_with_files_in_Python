# Напишите код, который переводит словарь d в формат JSON.
# Результат запишите в файл file.json.

d = {
    "data": [
        {
            "id": 1,
            "name": "Antony"
        },
        {
            "id": 2,
            "name": "Vladik"
        },
        {
            "id": 3,
            "name": "Ivan"
        }
    ]
}
# ваш код ниже
import json

with open("file.json", "w") as f:
    json.dump(d, fp=f)

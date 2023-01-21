# Вам дана следующая структура файла в формате JSON:
# [
# {
#     "id": 1,
#     "login": "gafgsd",
#     "password": "gsdffsd",
#     "email": "sh@ya.ru",
#     "date": "2022-12-12",
#     "status": 2,
#     "is_moderator": false
# }
# ]
# Вам известно, что за поля должны к вам приходить, и какое должно быть в них содержимое:
# id – int, обязательное
# login – str, обязательное, минимальная длина 3 и максимальная 20 символов
# password – str, обязательное, минимальная длина 3 и максимальная 50 символов, имеется хотя
# бы одна цифра и буква в верхнем регистре
# email – str, опциональное, подходит под шаблон: {a}@{b}.{c}
# date – str, опциональное, дата в формате ISO – YYYY-mm-dd
# status – int, обязательное, один из статусов 1,5,7,9,14
# is_moderator – bool, опциональное
# Отвалидируйте файл file.json. В качестве результата для каждого пользователя в случае если
# все в порядке запишите OK, в ином случае строку Failed. Ответы записывайте через запятую.
# Failed,OK,...

from pydantic import BaseModel, constr, parse_obj_as, EmailStr, validator
from datetime import date
import json


class User(BaseModel):
    id: int
    login: constr(min_length=3, max_length=20)
    password: constr(min_length=3, max_length=50)
    email: EmailStr | None
    date: date | None
    status: int
    is_moderator: bool | None

    @validator("password")
    def password_has_upper_letter(cls, v: str):
        assert not v.islower()
        return v

    @validator("password")
    def password_has_digit(cls, v: str):
        assert any([l.isdigit() for l in v])
        return v

    @validator("status")
    def status_validate(cls, v: int):
        assert v in (1, 5, 7, 9, 14)
        return v


answer = []
with open('file.json') as file:
    for user in json.load(file):
        try:
            user_obj = parse_obj_as(User, user)
            answer.append('OK')
        except:
            answer.append('Failed')

print(','.join(answer))

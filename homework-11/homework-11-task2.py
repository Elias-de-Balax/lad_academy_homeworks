"""
Профиль в JSON. Создать словарь с данными человека (имя, возраст, город, список любимых книг) и сохранить его в
profile.json через json.dump с ensure_ascii=False и indent. Затем прочитать файл через json.load и вывести входящие в
него данные.
"""

import json

profile = {
    "name": "Илья",
    "age": 48,
    "city": "Москва",
    "books": ["Fantasy", "Programming"],
}

with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(profile, f, ensure_ascii=False, indent=2)

with open("profile.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("Имя:", loaded["name"])
print("Возраст:", loaded["age"])
print("Город:", loaded["city"])
print("Книги:", loaded["books"])
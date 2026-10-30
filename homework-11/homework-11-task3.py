"""
Экспорт статей в CSV. Взять список словарей (заголовок, автор, просмотры) и записать его в blog.csv через csv.writer.
Потом прочитать файл через csv.reader и вывести каждую строку. Убедиться, что CSV корректно открывается в табличном
редакторе.
"""

import csv

rows = [
    ["title", "author", "views"],
    ["Первая статья", "Иван", 120],
    ["Вторая статья", "Анна", 350],
    ["Третья статья", "Пётр", 90],
]

with open("blog.csv", "w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(rows)

with open("blog.csv", "r", encoding="utf-8") as f:
    f.readline() # Чтобы не выводить заголовок
    reader = csv.reader(f)

    for i, row in enumerate(reader, start=1):
        print(f"{i}. {row}")
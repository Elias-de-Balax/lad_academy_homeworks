"""
«Красивый список постов». В файле blog.py дополните классы Author, Post, Category методами __str__ и __repr__
(как в Этапе 1). Соберите в main.py блог из 3–4 постов, разбейте на пару категорий (например, «Новости», «IT») и
выведите каждую категорию отдельным аккуратным блоком. Убедитесь, что print(post) и print(posts) дают разный вывод —
и коротко комментарием в коде объясните, почему.
"""

from blog import Author, Post, Category

posts = [
    Post("Введение в Django",
         "Введение в Django",
         Author("Василий", "example@gmail.com")),
    Post("Списки в Python",
         "Списки в Python",
         Author("Сергей", "mail@yandex.ru")),
    Post("Как установить uv",
         "Как установить uv",
         Author("Иван","mail@gmail.com")),
    Post("Применение Django в Web",
         "Применение Django в Web",
         Author("Петр", "example@mail.ru"))
]

categories = [Category("Новости"), Category("IT")]
categories[0].append(posts[0])
categories[0].append(posts[1])
categories[1].append(posts[2])
categories[1].append(posts[3])

for category in categories:
    print(f"{category}\n")

print(posts[0])
print(posts) # Списки выводятся только через repr, чтобы их вывести "по-человечески", надо оформить цикл
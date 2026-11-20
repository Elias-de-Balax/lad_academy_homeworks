"""
4. Добавить генератор для экспорта. Напишите функцию-генератор iter_posts(posts) через yield, которая по одному отдаёт
посты (или строки постов). Покажите использование и в for, и через next().
"""

from typing import Iterable

def iter_posts(posts: list[str]) -> Iterable[str]:
    for post in posts:
        yield post

posts = ["Первый пост", "Второй пост", "Третий пост"]

print("Через for:")
for post in iter_posts(posts):
    print(post)

print("\nЧерез next():")
generator = iter(posts)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator, "Нет постов"))

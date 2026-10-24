"""Каталог статей (namedtuple). Определить Post с полями title, category, year. Создать список из 4 статей.
    Реализовать: вывести все статьи, отсортировать по году по убыванию, найти и вывести статьи заданной категории,
    добавить новую статью. Оформить вывод через f-строки."""

from collections import namedtuple

Post = namedtuple("Post", ["title", "category", "year"])

input_posts = [Post("Как установить uv", "Инструментарий", 2026),
               Post("Списки в Python", "Python", 2025),
               Post("Введение в Django", "Django", 2025),
               Post("Применение Django в Web", "Django", 2024)]

sorted_posts = sorted(input_posts, key=lambda post: post.year, reverse=True)

print("Отсортированный по убыванию список по году:")
for post in sorted_posts:
    print(f"{post.title:25s} | {post.category:25s} | {post.year}")

input_category = input("\nВведите категорию: ")

#filtered_posts = [post for post in input_posts if post.category.lower() == input_category.lower()]
#filter - как пример аналогичной реализации, но он медленнее list comprehension из-за накладных расходов на функции
filtered_posts = list(filter(lambda post: post.category.lower() == input_category.lower(), input_posts))

if filtered_posts:
    for post in filtered_posts:
        print(f"{post.title:25s} | {post.category:25s} | {post.year}")
else:
    print(f"Постов в категории «{input_category}» нет.\n")

print("\nОбновленный список:")
input_posts.append(Post("Введение в FastAPI", "FastAPI", 2026))
for post in input_posts:
    print(f"{post.title:25s} | {post.category:25s} | {post.year}")
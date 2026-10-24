"""Группировка по категории. Для того же каталога статей сгруппировать заголовки по категории с помощью defaultdict
    из collections, а затем посчитать количество статей в каждой категории через Counter. Вывести оба результата."""

from collections import Counter, defaultdict, namedtuple

Post = namedtuple("Post", ["title", "category", "year"])

input_posts = [Post("Как установить uv", "Инструментарий", 2026),
               Post("Списки в Python", "Python", 2025),
               Post("Введение в Django", "Django", 2025),
               Post("Применение Django в Web", "Django", 2024)]

posts_grouped = defaultdict(list)
for post in input_posts:
    posts_grouped[post.category].append(post.title)

for category, posts in posts_grouped.items():
    print(f"{category}: {posts}")

category_counter = Counter([post.category for post in input_posts])
print("\nЧастота постов по категориям:", dict(category_counter))
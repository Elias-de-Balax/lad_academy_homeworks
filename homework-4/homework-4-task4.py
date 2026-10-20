"""Поиск по блогу. Есть список заголовков постов. Вывести только те, что содержат слово "Python" (через find или in).
   Затем для каждого заголовка вывести его slug через написанную на занятии функцию build_slug."""

def build_slug(title: str) -> str:
    """Преобразует заголовок поста в url-friendly slug."""
    result = title.lower().replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or (char == "-"):
            clean.append(char)
        else:
            clean.append("-")

    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    return result.strip("-")

posts = ["Почему Django лучше всего изучать на практике!",
         "Разработка  на Python   требует практики",
         "    Я люблю программировать на Python.",
         "Как настроить Django под продакшен"]

for post in posts:
    if -1 != post.find("Python"):
        print(f"Исходная строка: {post}")
        print(f"Slug строки: {build_slug(post)}\n")
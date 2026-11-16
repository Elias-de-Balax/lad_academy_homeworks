"""
1. Базовый класс + два наследника на данных блога. Создайте абстрактный класс Content с полями title и created_at и
абстрактным методом get_summary(). Реализуйте наследников Post(title, body, author) и Page(title, slug) с
super().__init__(). В get_summary() выведите краткое описание каждого.

2. Переопределение и super(). Для Post переопределите get_summary(), дополнив родительскую версию через super() (например,
добавьте длину текста). Для Page — верните полностью свою реализацию. Вызовите метод у экземпляров обоих классов и
сравните вывод.
"""

from datetime import datetime
from typing import override

class Content:
    def __init__(self, title: str) -> None:
        self.title = title
        self.created_at = datetime.now().strftime("%d.%m.%Y")

    def get_summary(self) -> str:
        return f"{self.title:25s}"

class Page(Content):
    def __init__(self, title: str, slug: str) -> None:
        super().__init__(title)

        self.slug = slug

    @override
    def get_summary(self) -> str:
        return f"{self.title:25s} | {self.slug:25s} | {self.created_at}"

class Post(Content):
    def __init__(self, title: str, body: str, author: str) -> None:
        super().__init__(title)

        self.body = body
        self.author = author

    @override
    def get_summary(self) -> str:
        return f"{super().get_summary():25s} | {self.body:25s} | {self.author:25s} | {self.created_at}"

if __name__ == "__main__":
    post = Post("Введение в Django", "Введение в Django", "Василий")
    page = Page("О проекте", "about")

    print(post.get_summary())
    print(page.get_summary())
    print()
    print(Content.__dict__) # для сравнения в задаче 6
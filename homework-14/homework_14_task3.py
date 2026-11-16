"""
Полиморфизм и duck typing. Напишите функцию render_all(items), которая принимает список объектов и вызывает у каждого
get_summary(). Заполните список постами и страницами и выведите результат. Затем дополнительно передайте в неё объект,
который не наследуется от Content, но имеет метод get_summary() (например, класс с __getattr__/собственным get_summary()),
— и покажите, что функция его тоже принимает. Это демонстрация duck typing.
"""

from homework_14_task1_2 import Post, Page

class Author:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def get_summary(self) -> str:
        return f"{self.name:25s} | {self.email}"

input_list = [Post("Введение в Django", "Введение в Django", "Василий"),
              Page("О проекте", "about"),
              Author("Василий", "example@gmail.com")]

def render_all(items) -> None:
    for item in items:
        print(item.get_summary())

if __name__ == "__main__":
    render_all(input_list)
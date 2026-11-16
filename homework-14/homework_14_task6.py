"""
Звёздочка (самостоятельное изучение abc и dataclasses). По официальной документации Python изучите
(https://docs.python.org/3/library/abc.html и https://docs.python.org/3/library/dataclasses.html): (а) чем ABC
отличается от обычного класса, (б) зачем нужен @abstractmethod, (в) как @dataclass упростил бы ваши классы Post/Page
(поля, __init__, __repr__ — без ручного кода). Напишите конспект на 5–8 предложений с примером кода, где Content описан
через @dataclass, и сравните с ручной версией. Это задел на следующее занятие.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import override

@dataclass
class Content(ABC):
    title: str = ""
    created_at: str = datetime.now().strftime("%d.%m.%Y")

    @abstractmethod
    def get_summary(self) -> str:
        pass

@dataclass
class Page(Content):
    slug: str = ""

    @override
    def get_summary(self) -> str:
        return f"{self.title:25s} | {self.slug:25s} | {self.created_at}"

@dataclass
class Post(Content):
    body: str = ""
    author: str = ""

    @override
    def get_summary(self) -> str:
        return f"{self.title:25s} | {self.body:25s} | {self.author:25s} | {self.created_at}"

post = Post(title="Введение в Django", body="Введение в Django", author="Василий")
page = Page(title="О проекте", slug="about")

print(post.get_summary())
print(page.get_summary())
print()
print(post)
print(page)
print()
print(Content.__dict__) # для сравнения в задаче 1_2

# ABC отличается от обычного класса механизмом наследования, временем проверки контракта и возможностью принудительного
# переопределения методов.
# Класс, наследуемый от АВС, и одновременно использующий декоратор @abstractmethod нельзя явно инициализировать и
# заставляет наследников реализовать все абстрактные методы.
# Декоратор dataclass упрощает написание кода класса, автоматически добавляет методы __(имя метода)__, необходимые
# для работы с классом, при этом словарь класса становится больше по сравнению с классом, методы у которого
# добавляются вручную.

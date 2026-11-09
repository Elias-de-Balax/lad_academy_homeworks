"""
«dataclass для комментариев». Создайте @dataclass class Comment с полями author, text, likes=0 и tags (через
field(default_factory=list)). Добавьте классу __post_init__: если text пустой — выбрасывать ValueError (дополнительная
валидация после авто-__init__). Проверьте, что: (а) Comment("А", "X") == Comment("А", "X") — True; (б) тег, добавленный
в один комментарий, не «протекает» в другой.
"""
from dataclasses import dataclass, field

@dataclass
class Comment:
    author: str
    text: str
    likes: int = 0
    tags: list = field(default_factory=list)

    def __post_init__(self):
        if not self.text or not self.text.strip():
            raise ValueError("Текст не может быть пустым")

try:
    comment1 = Comment("Василий", "   ")
except ValueError as e:
    print(f"Ошибка: {e}")

comment2 = Comment("Василий", "Введение в Django", tags=["django"])
comment3 = Comment("Василий", "Введение в Django", tags=["django"])
comment4 = Comment("Петр", "Списки в Python", tags=["python", "web"])

print(comment3 == comment2)

comment3.tags.append("web")

print(comment2.tags)
print(comment3.tags)
print(comment4.tags)
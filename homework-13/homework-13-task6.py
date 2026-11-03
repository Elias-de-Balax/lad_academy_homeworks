"""
Звёздочка (самостоятельное изучение). Изучите по официальной документации Python волшебные методы __str__ и __repr__.
Определите их в классе Book так, чтобы print(book) выводил красивую строку («Война и мир» — Лев Толстой), а в REPL по
имени переменной (book) — «внутреннее» представление (Book(title='Война и мир', author='Лев Толстой', year=1869)).
Опишите коротким комментарием, чем они отличаются и какой из них обычно переопределяют в Django-моделях. (Опционально,
для тех, кто быстро справился, — посмотрите, что даёт @dataclass для такого класса, и оставьте вывод в комментарии.)
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"\"{self.title}\" - {self.author}, {self.year} год"

    def __repr__(self):
        return f"Book(title=\"{self.title}\", author={self.author}, year={self.year})"

book = Book("Война и мир", "Лев Толстой", "1869")

print(book)
print(repr(book))

# __str__ - для вывода информирования об объекте пользователю, его чаще переопределяют в Django для информативности
# __repr__ - для вывода информации для логгирования и отладки

from dataclasses import dataclass

@dataclass
class BookEx:
    title: str
    author: str
    year: int

book = BookEx("Война и мир", "Лев Толстой", "1869")

print()
print(book)
print(repr(book))

# декоратор dataclass автоматически генерирует методы __init__, __repl__ и тд на основе заданных полей
# @dataclass(frozen=True) превращает экземпляр класса в аналог кортежа и добавляется метод __hash__ для хеширования


"""
«Библиотека» со классом Book. Класс Book с title, author, year; методы is_old() (возвращает True, если книга старше 10
лет) и display(). Атрибут класса genre = "Художественная литература". Создать 3–4 книги, вывести их и пометить «старые».
Добавить атрибут класса category_count и объяснить в комментарии разницу между ним и атрибутами экземпляра.
"""
import datetime as dt

class Book:
    genre = "Художественная литература"
    category_count = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        Book.category_count += 1

    def is_old(self):
        return dt.datetime.now().year-self.year > 10

    def display(self):
        return (f"Название: {self.title}, "
                f"Автор: {self.author}, "
                f"Год выпуска: {self.year}")

books = [Book("Списки в Python", "Владимир Дронов", 2015),
         Book("Введение в Django", "Гарри Персиваль", 2020),
         Book("Применение Django в Web", "Арун Равиндран", 2025),
         Book("Введение в FastAPI", "Себастьян Рамирес", 2014)]

for book in books:
    print (f"{book.display()} {"(старая книга)" if book.is_old() else ""}")

print(Book.category_count)

# Разница между атрибутами класса и атрибутами экземпляра заключается в их жизненном цикле, аттрибут класса существует
# в единственном экземпляре - в самом классе и доступ к нему осуществляется через имя класса, тогда как атрибуты
# экземпляра через self
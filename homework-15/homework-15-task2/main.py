"""
«Контролируемая модель поста». Перепишите Post так, чтобы заголовок хранился в self._title, а наружу отдавался через
@property с сеттером-валидацией (не пустой, обрезка пробелов). Добавьте вычисляемые свойства: title_length (длина
заголовка) и slug (заголовок в нижнем регистре, пробелы → дефисы; например, «Мой Первый Пост» → мой-первый-пост).
Продемонстрируйте, что запись пустого заголовка поднимает ValueError.
"""

from blog import Author, Post

post = Post("Введение в Django","Введение в Django", Author("Василий", "example@gmail.com"))

print("Заголовок:", post.title)
print("Длина заголовка:", post.title_length)
print("Slug:", post.slug)

try:
    post.title = "   "
except ValueError as e:
    print(f"Ошибка: {e}")

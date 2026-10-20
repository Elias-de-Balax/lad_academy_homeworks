"""Звёздочка (самостоятельное изучение key=lambda). Изучите по официальной документации Python, как работает
   sorted(..., key=...) и что такое lambda. Отсортируйте список постов из задачи 3: а) по длине заголовка;
   б) по категории (по алфавиту); в) по заголовку в обратном порядке. Объясните комментарием в коде, что возвращает
   key-функция в каждом случае."""

input_posts = [
    ["2026-02-18", "Как установить uv", "Инструментарий"],
    ["2026-02-22", "Списки в Python", "Python"],
    ["2026-02-10", "Введение в Django", "Django"],
    ["2026-02-25", "Применение Django в Web", "Django"]
]

sorted_posts1 = sorted(input_posts, key=lambda x: len(x[1])) # key возвращает в качестве ключа длину заголовка
sorted_posts2 = sorted(input_posts, key=lambda x: x[2]) # key возвращает в качестве ключа категорию
sorted_posts3 = (
    sorted(input_posts, key=lambda x: x[1], reverse=True)) # key возвращает в качестве ключа заголовок

print("Сортировка по длине заголовка:")
for row in sorted_posts1:
    print(row)

print("\nСортировка по категории (по алфавиту):")
for row in sorted_posts2:
    print(row)

print("\nСортировка по заголовку в обратном порядке:")
for row in sorted_posts3:
    print(row)
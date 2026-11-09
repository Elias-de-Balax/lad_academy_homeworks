"""
б) в **contextlib**: найдите @contextmanager и напишите свой контекстный менеджер (например,
@contextmanager def open_log(...)), который печатает «открыли»/«закрыли» при входе в with и выходе из него.
Запишите оба вывода комментариями в коде. Обе темы более подробно пригодятся в занятии 17.
"""

from contextlib import contextmanager

@contextmanager
def open_log(filename: str, mode: str = 'a'):
    print(f"Открываем log-файл {filename}...")

    f = open(filename, mode, encoding="utf-8")

    try:
        yield f
    finally:
        f.close()

        print(f"Закрыли log-файл {filename}\n")


with open_log("log.txt", "a") as log:
    log.write("Добавляем новый лог...\n")

try:
    with open_log("log1.txt", "r") as log:
        print(log.read())
except FileNotFoundError as e:
    print(f"Файл {e.filename} не найден")

# декоратор contexmanager позволяет использовать собственную генераторную функцию в качестве контекстного менеджера



"""
5. Звёздочка (генератор / itertools). Реализуйте функцию, которая лениво читает большой файл (например, big.log
размером >1 ГБ вы можете сгенерировать утилитой, или взять имеющийся) и считает, сколько строк содержат заданное слово,
не загружая файл целиком. Дополнительно: используйте itertools.chain для объединения строк из нескольких файлов и
itertools.count для нумерации найденных строк. Подсказка: решение в генераторе + for + проверка word in line.
"""

from typing import Iterator
from itertools import chain, count

def read_file(path: str) -> Iterator[str]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.rstrip()

def find_word(word: str, files: list[str]) -> Iterator[tuple[int, str]]:
    all_lines = chain.from_iterable(read_file(file) for file in files)
    finded_lines = (line for line in all_lines if word.lower() in line.lower())

    for num, line in zip(count(1), finded_lines):
        yield num, line

try:
    for num, line in find_word("мир", ["text_1.txt", "text_2.txt"]):
        print(num, line)
except StopIteration:
    print("Произошла ошибка в итерации строк из файла")
except FileNotFoundError as e:
    print(f"\nФайл {e.filename} не найден")
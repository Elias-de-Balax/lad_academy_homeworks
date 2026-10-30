"""
Заметки. Создать программу, которая принимает от пользователя текст и дописывает его в файл notes.txt (режим "a"), а
затем читает весь файл и выводит его с номерами строк.
"""

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Моя первая заметка\n")
    f.write("Вторая заметка\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        print(f"Строка {i}:", line.strip())
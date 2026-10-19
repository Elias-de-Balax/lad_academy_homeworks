"""Счётчик слов. Дана строка с текстом поста. Разбить её на слова через split(), вывести количество слов и первое слово
   в верхнем регистре (upper())."""

str_ = input("Введите строку: ")

if str_:
    for char in [',', '.', '-']:
        str_ = str_.replace(char, ' ')

    words = str_.split()
    print(words)
    print(f"Количество слов: {len(words)}")

    if len(words):
        print(words[0].upper())
else:
    print("Строка не введена.")
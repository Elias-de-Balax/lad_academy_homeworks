"""Звёздочка ★ — сумма и произведение через цикл. Напишите программу, которая считает произведение чисел от 1 до n
   факториал n!) через for. Например, для n = 5 получится 1*2*3*4*5 = 120. Затем дополнительно выведите через вложенные
   циклы (цикл внутри цикла) таблицу умножения from 1 to 5 в виде строк. Подсказка: внешний цикл — по множителю i,
   вложенный — по j"""

UNKNOWN = -1

try:
    n = int(input("Введите число: "))

    if n < 0:
        raise ValueError
except ValueError:
    print("Неверно введенное значение.")
    n = UNKNOWN

if n != UNKNOWN:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"\nФакториал {n}! = {factorial}")

    print(f"\nТаблица умножения от 1 до {n}:")
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            composition = i * j
            row += f"{i}*{j}={composition:2d}  "

        print(row)
"""Декоратор с «полезной нагрузкой». Напишите декоратор @time_it, но примените его к функции, которая сортирует список
    (например, sorted(data)). Затем напишите функцию с тем же результатом, но без декоратора, и сравните, насколько
    важно возвращать результат. Подсказка: если забыть return result, функция вернёт None, и это сразу видно."""

import random
from homework_9_task2 import time_it

list = random.sample(range(1, 101),20)

@time_it
def sort_list(list: list) -> list:
    return sorted(list)

def sorted_list(list: list) -> list:
    return sorted(list)

print("Исходный список:", list)
print("Отсортированный список 1:", sort_list(list)) # если в декораторе забыть return result, функция вернёт None
print("Отсортированный список 2:", sorted_list(list))
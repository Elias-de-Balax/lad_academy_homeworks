"""Список чисел и статистика. Создайте список из 6–8 чисел (например, баллы за тест). Выведите сумму (sum), минимальное
   и максимальное значение, среднее (сумма / длина) и список, отсортированный по убыванию."""

import random

input_list = random.sample(range(0, 100), 8)

print("Исходный список:", input_list)
print("Сумма всех чисел:", sum(input_list))
print("Минимальное значение:", min(input_list))
print("Максимальное значение:", max(input_list))
print("Среднее значение:", round(sum(input_list)/len(input_list), 2))
print("Список, отсортированный по убыванию: ", sorted(input_list, reverse=True))

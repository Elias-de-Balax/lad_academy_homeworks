"""Цены и «доступность». Дан список цен. Порог вводится с клавиатуры. Через comprehension постройте список флагов
   True/False — цена меньше порога. Посчитайте, сколько цен ниже порога (sum(flags)), и выведите среднюю цену только по
   «доступным» позициям."""

import random

UNKNOWN = 0

price_list = random.sample(range(1, 1000), 20)
print("Текущие цены:", price_list)

try:
    input_threshold = int(input("Введите порог цен: "))

    if input_threshold <= 0:
        raise ValueError
except ValueError:
    print("Неверно введенное значение.")
    input_threshold = UNKNOWN

if UNKNOWN != input_threshold:
    threshold_flags = [price < input_threshold for price in price_list]
    threshold_prices = [price for price, flag in zip(price_list, threshold_flags) if flag]

    print(f"Количество цен ниже порога: {sum(threshold_flags)}")
    print("Цены ниже порога:", threshold_prices)
    print("Средняя цена:",
          round(sum(threshold_prices)/len(threshold_prices), 2) if len(threshold_prices) > 0 else UNKNOWN)
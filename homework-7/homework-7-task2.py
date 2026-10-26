"""**Распаковка и *rest.** Дан кортеж numbers = (10, 20, 30, 40, 50). Распаковать: первое число, «середину» через
    *middle и последнее число. Вывести их. Затем распаковать строку name = "Иван" в first, *rest и напечатать
    результат."""

numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers

print(f"{first}, \n{middle}, \n{last}")

name = "Иван"
first, *rest = name

print(f"\n{first}, \n{rest}")
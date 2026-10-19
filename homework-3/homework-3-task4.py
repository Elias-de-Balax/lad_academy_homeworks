"""Только чётные. Вывести все чётные числа от 1 до 100 через for в сочетании с range и continue (нечётные пропускать)."""

str_ = ""
for i in range(1, 101):
    # Как вариант, чем через ветвление с continue
    str_ += str(i) if not (i % 2) else " "

print(str_)
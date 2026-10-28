"""Звёздочка (продвинутая). Самостоятельное изучение @lru_cache и @property.
    Для @lru_cache: найдите его в документации functools и напишите функцию fibonacci с кэшированием, затем ту же функцию
    без кэша. Сравните время выполнения для n = 30 (через time.perf_counter()) и объясните комментарием, почему с кэшем
    быстрее.
"""

import functools
from homework_9_task2 import time_it

@functools.lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_recursive(n: int) -> int:
    if n < 2:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

@time_it
def fibonacci_cached(n: int) -> int:
    return fibonacci(n)

@time_it
def fibonacci_nocached(n: int) -> int:
    return fibonacci_recursive(n)

print(fibonacci_cached(30))
print(fibonacci_nocached(30))

# Насколько я понимаю, при кэшировании уникальные значения вычисляются 1 раз, без кэша - миллионы
# По классификации big O, с кэшем - O(n), без - O(2^n)
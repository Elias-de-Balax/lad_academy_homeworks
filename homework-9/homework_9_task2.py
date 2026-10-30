"""Декораторы @time_it и @logged. Напишите оба декоратора с @functools.wraps. Примените @time_it к функции,
    рассчитывающей сумму элементов списка, и @logged к функции, формирующей приветствие. Убедитесь, что метаданные
    (__name__, __doc__) сохранены и что декораторы возвращают исходный результат функции (а не None)."""

import functools
import time

def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"> Функция {func.__name__} отработала за {end - start:.6f} с.")
        return result

    return wrapper

def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"> Вызов {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"> Завершение {func.__name__} -> {result}")
        return result

    return wrapper

@time_it
def sum_elements(arg_list):
    """Выводит сумму элементов списка."""
    return sum(arg_list)

@logged
def greet(name):
    """Простое приветствие."""
    return f"Привет, {name}!"

if __name__ == "__main__":
    print(sum_elements.__name__)
    print(sum_elements.__doc__)
    print(greet.__name__)
    print(greet.__doc__)

    print()
    print(sum_elements(range(100)))
    print(greet("мир"))
"""Замыкания. Напишите функцию make_power(exponent), которая возвращает функцию power(base) (вычисляет base ** exponent).
    Затем напишите make_counter(start) со nonlocal, как на семинаре. Протестируйте обе и выведите результаты в консоль.
    Подсказка: возвращайте функцию, а не результат её вызова."""

def make_power(exponent):
    def power(base):
        return base ** exponent

    return power

def make_counter(start):
    count = start

    def inc(step = 1):
        nonlocal count
        count += step

        return count

    return inc

power1 = make_power(2)
power2 = make_power(3)

print(power1(10))
print(power2(10))

counter = make_counter(10)

print()
print(counter(10))
print(counter(10))
print(counter(10))
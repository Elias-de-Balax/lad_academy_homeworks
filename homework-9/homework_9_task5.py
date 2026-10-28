"""Звёздочка. Декоратор с аргументами. Напишите декоратор @repeat(times), который вызывает функцию N раз (@repeat(3)).
    Это потребует «фабрики декоратора»: repeat(times) возвращает декоратор, а тот возвращает обёртку. Подсказка (та же
    логика, что в @api_view(["GET"])):
    Разберите каждую вложенную функцию и объясните комментарием, почему цепочка «repeat(times) → decorator → wrapper»
    нужна именно такая. Проверьте на функции, печатающей текст."""

import functools

def repeat(times= 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def print_helloworld():
    print("Hello world!")

print_helloworld()

# Основная функция декоратора принимает только саму функцию, чтобы добавить дополнительные параметры в декоратор,
# необходим еще один верхний слой-посредник. Эти доп. параметры замыкаются в decorator и передаются дальше во вложенные
# функции, поэтому действует такая цепочка
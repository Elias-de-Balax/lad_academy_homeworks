"""
Звёздочка (повышенная сложность). Изучите по официальной документации Python цепочку исключений — конструкцию
raise ... from e — и иерархию встроенных исключений (от BaseException до Exception и ниже). Приведите в комментарии
пример, где raise NewError from original_error полезен (сохранить исходную причину), и коротко опишите, какие типы
исключений стоит ловить, а какие — нет (например, зачем избегать except BaseException и слепого except:).
"""

class NewValueError(Exception):
    """Пользовательский тип ошибки"""
    pass

try:
    try:
        raise ValueError("Первое исключение")
    except ValueError as e:
        raise NewValueError("Второе исключение") from e
except NewValueError as e:
    print(f"Перехваченное исключение {e.__class__.__name__}: {e.__str__()}")
    print(f"Ошибка, которая вызвала первое исключение {e.__cause__.__class__.__name__}: {e.__cause__.__str__()}")

"""
except BaseException и слепой except перехватывает все исключения, включая системные, при этом программа может зависнуть
except Exception - общее исключение программы (базовый класс исключений программы), уместно ставить там, где main()
"""
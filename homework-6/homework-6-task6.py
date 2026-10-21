"""6. Множества + OrderedDict. Реализуйте функцию, которая принимает список и возвращает первые вхождения элементов
    но без повторов и сохранив порядок — например, из ["b", "a", "b", "c", "a"] должно получиться ["b", "a", "c"].
    Это удобно сделать множеством (set) для проверки «видели ли уже» в связке со списком-результатом. Затем
    самостоятельно изучите collections.OrderedDict по официальной документации
    (https://docs.python.org/3/library/collections.html#collections.OrderedDict) и коротко опишите в комментарии кода:
    что это такое, зачем он нужен и чем отличается от обычного dict в современном Python (начиная с 3.7)."""

from collections import OrderedDict

#input_list = ["b", "a", "b", "c", "a"]
input_list = ["uv", "python", "django", "python", "web", "python", "uv"]

def get_ordered_list(arg_list: list) -> list:
    return list(OrderedDict({value: None for value in arg_list}))

print("Список через set:", list(set(input_list)))
print("Список через OrderedDict:", get_ordered_list(input_list))

# Как я понимаю, что OrderedDict гарантированно сохраняет порядок вставки элементов в отличие от dict
# Два идентичных словаря с разностоящими элементами при сравнении в dict даст True, a OrderedDict даст False
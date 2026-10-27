"""
(со звёздочкой, продвинутая). Коротко изучите по документации модуль functools (функции lru_cache, partial, wraps)
    или базовое понятие рекурсии (функция, вызывающая саму себя, например, факториал или поиск по вложенному списку).
    Опишите своими словами комментарием в коде, что вы выбрали и зачем, и приведите рабочий пример. Важно: декораторы
    полноценно разбираются на занятии 9 — сейчас просто «познакомьтесь» и зафиксируйте наблюдение.
"""

# Пример рекурсивной функции на примере вложенного списка

nested_list = [1, [2, 3], [4, [5, 6]], 7]

def find_in_nestedlist(arg_list, target):
    for element in arg_list:
        if element == target:
            return True
        elif type(element) is list:
            if find_in_nestedlist(element, target):
                return True

    return False

print(find_in_nestedlist(nested_list, 3))
print(find_in_nestedlist(nested_list, 6))
print(find_in_nestedlist(nested_list, 10))
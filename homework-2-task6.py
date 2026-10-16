"""Звёздочка (истинность и bool()). Исследуйте, какое значение даёт bool() для: 0, 0.0, "", "0", [], [1], None, {}, False.
   Соберите таблицу «значение → bool() → True/False» и отдельно объясните, почему bool("0") — True, а bool(0) — False.
   Придумайте и опишите в комментариях пример, где непонимание «истинности» привело бы к логической ошибке (например,
   проверка if text: вместо if text is not None:)."""

print(f"0 -> bool(0) -> {bool(0)}") # Значение равно 0 как int, а это всегда False
print(f"0.0 -> bool(0.0) -> {bool(0.0)}")
print(f""""" -> bool("") -> {bool("")}""")
print(f""""0" -> bool("0") -> {bool("0")}""") # Непустая строка
print(f"[] -> bool([]) -> {bool([])}")
print(f"[1] -> bool([1]) -> {bool([1])}") # Непустой массив
print(f"None -> bool(None) -> {bool(None)}")
str_ = "{}"
print(f"{str_} -> bool({str_}) -> {bool({})}")
print(f"False -> bool(False) -> {bool(False)}")

# Проверка на логические ошибки
int_: int = None
print(f"\n{bool(int_ is None)}, {bool(int_)}")


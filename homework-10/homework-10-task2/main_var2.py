"""Напиши модуль utils.py и продемонстрируй разные способы импорта. Создай файл utils.py с двумя-тремя полезными
    функциями (например, проверка чётности, преобразование строки в число с обработкой ошибки). Затем в двух разных
    файлах-заготовках подключи его: в первом — import utils, во втором — from utils import ... as .... Обрати внимание
    на разницу в вызове."""

from utils import str_to_int as to_int
from utils import is_parity as parity

if __name__ == "__main__":
    print(to_int("20"))
    to_int("qq")
    parity("s21")
    print(parity(20))
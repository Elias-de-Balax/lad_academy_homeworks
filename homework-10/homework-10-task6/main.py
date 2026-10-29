"""
Звёздочка (самостоятельное изучение datetime): изучи официальную документацию Python по модулю datetime. Напиши
программу, которая выводит текущую дату в трёх разных форматах: 28.08.2026, 2026-08-28, 28 августа 2026. Используй
strftime() с подстановками %d, %m, %Y, %B. Полезно: datetime.datetime.now(), now.strftime("%d.%m.%Y"),
datetime.strptime(...).
"""

import datetime
import locale as lc

try: # Для Linux/macOS
    lc.setlocale(lc.LC_TIME, 'ru_RU.UTF-8')
except lc.Error:
    try: # Для Windows
        lc.setlocale(lc.LC_TIME, 'Russian_Russia.1251')
    except lc.Error:
        print("Русская локаль не установлена в вашей операционной системе.")

dt_now = datetime.datetime.now()

print(dt_now.strftime("%d.%m.%Y"))
print(dt_now.strftime("%Y-%m-%d"))
print(dt_now.strftime("%d %B %Y"))

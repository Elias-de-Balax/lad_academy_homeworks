"""
Подключи стороннюю библиотеку через uv add. Добавь в проект любую библиотеку (например, rich или colorama) и примени её
в выводе своей программы. Загляни в pyproject.toml и объясни в комментарии в коде, что там появилось и зачем это нужно.

Было до uv add rich

[project]
name = "lad-academy-homeworks"
version = "0.1.0"
requires-python = ">=3.15"
dependencies = [
    "ruff>=0.17.1",
]

Стало после uv add rich

[project]
name = "lad-academy-homeworks"
version = "0.1.0"
requires-python = ">=3.15"
dependencies = [
    "rich>=15.0.0", # добавлена библиотека rich в проект и установка её в окружение
    "ruff>=0.17.1",
]

библиотека rich нужна для оформления вывода данных в консоли

"""


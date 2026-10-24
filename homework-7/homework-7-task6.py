"""Звёздочка (продвинутая) — dataclasses.dataclass. Самостоятельно изучите по официальной документации Python декоратор
    @dataclass из модуля dataclasses и коротко (3–4 предложения) опишите, чем он похож на namedtuple и чем отличается:
    mutability, значения по умолчанию, поддержка type hints, наличие asdict(). Приведите маленький пример класса Post
    через @dataclass и укажите, в каких случаях вы выбрали бы dataclass, а в каких — namedtuple."""

"""
Фабрика namedtuple и декоратор @dataclass создают похожую структуру объекта при инициализации и поддерживают доступ
к полям по атрибуту. Основная разница в том, что namedtuple создает неизменяемый объект, @dataclass - изменяемый
У класса, созданного с помощью декоратора больше возможностей для последующей обработки, а объект, созданный
namedtuple представляется как обертка над кортежем и меньше занимает память/выше производительность
Следовательно, если нужны неизменяемые типы данных и эффективные возможности их обработки, то namedtuple, 
иначе @dataclass
"""

from dataclasses import asdict, dataclass

@dataclass
class Post:
    title: str
    category: str = "Unknown"
    year: int = 1899

input_post = Post("Неизвестная статья")
post_dict = asdict(input_post)

print("Тестовый пример:")
print(f"{input_post.title:25s} | {input_post.category:25s} | {input_post.year}")
print("Словарь:", post_dict)
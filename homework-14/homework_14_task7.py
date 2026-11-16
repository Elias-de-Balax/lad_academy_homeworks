"""
Звёздочка (Protocol вместо ABC). Возьмите контракт из задания 1 (метод get_summary()) и опишите его как Protocol
(class Summarizable(Protocol)). Покажите, что Post и Page удовлетворяют протоколу без наследования от него, а функция
render_all(items: list[Summarizable]) корректно их принимает. Добавьте @runtime_checkable и проверьте isinstance(Post(),
Summarizable). В комментариях объясните, в чём выгода Protocol перед ABC именно в этом случае. Посмотрите в typing
(https://docs.python.org/3/library/typing.html) раздел про Protocol.
"""
from typing import Protocol, runtime_checkable

from homework_14_task1_2 import Post, Page
from homework_14_task3 import Author

@runtime_checkable
class Summarizable(Protocol):
    def get_summary(self) -> str:
        pass

def render_all(items: list[Summarizable]) -> None:
    for item in items:
        if isinstance(item, Summarizable):
            print(item.get_summary())

input_list = [Post("Введение в Django", "Введение в Django", "Василий"),
              Page("О проекте", "about"),
              Author("Василий", "example@gmail.com")]

render_all(input_list)

# Protocol удобен, когда не нужно иметь общей реализации, а достаточно набора функций (контракта), те уменьшается
# связность объектов между собой. А также нивелируются возможные проблемы MRO
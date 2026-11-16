"""
Звёздочка (самостоятельное изучение): __slots__ и **contextlib**. Самостоятельно разберитесь:
а) в __slots__: перепишите маленький класс (например, Point с двумя координатами) на __slots__, объясните, какая
экономия памяти и какие ограничения появляются (нельзя добавить атрибут p.z). Замерьте разницу в памяти через
sys.getsizeof для тысяч объектов.
"""

import sys

class PointDict:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = PointDict(1, 2)
point2 = PointSlots(1, 2)

try:
    # Проверка наличия __dict__
    print(point1.__dict__)
    print(point2.__dict__)  # Вызывает ошибку AttributeError: 'PointSlots' object has no attribute '__dict__'
except AttributeError as e:
    print("Ошибка:", e)

try:
    # Проверка добавления нового атрибута
    point1.z = 3
    point2.z = 5 # 'PointSlots' object has no attribute 'z' and no __dict__ for setting new attributes
except AttributeError as e:
    print("Ошибка:", e)

print(sys.getsizeof(PointDict))
print(sys.getsizeof(PointSlots))
print(sys.getsizeof(point1))
print(sys.getsizeof(point2))

points1 = [PointDict(i, i) for i in range(1000)]
points2 = [PointSlots(i, i) for i in range(1000)]

print(sum(sys.getsizeof(point) for point in points1))
print(sum(sys.getsizeof(point) for point in points2))

# getsizeof не может в лоб определить точный размер экземпляра без __slots__, поэтому замер памяти будет некорректным,
# но если пошерстить __dict__ и его values, а также значения в полях, можно добиться приблизительного размера экземпляра,
# либо использовать какую-либо стороннюю библиотеку
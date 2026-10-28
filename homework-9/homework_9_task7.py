"""Для @property: кратко изучите, как декоратор превращает метод в «свойство» (доступ obj.field вместо вызова
    obj.field()). Напишите класс с приватным атрибутом и свойством-геттером (и, при желании, сеттером), выводящим
    валидированное значение. Объясните комментарием, что делает декоратор. Это подготовка к блоку ООП."""

class Object:
    def __init__(self, value: int):
        self.field = value

    _field: int = 0

    @property
    def field(self): # Декоратор @property делает этот метод доступным как поле-атрибут класса obj.field
        return self._field
    @field.setter
    def field(self, value: int):
        if type(value) is not int:
            raise TypeError('Значение field должно быть целочисленным')

        self._field = value

try:
    obj = Object(1)
    print(obj.field)
    obj.field = 5
    print(obj.field)
    # Почему при явном указании типа в сеттере все равно проглатываются другие типы данных и приходится
    # проверять на валидацию переменных? Я в курсе про неявное преобразование, но раз явно указан тип, должен быть
    # запрет на это
    obj.field = "6"
except TypeError as e:
    print(e.__str__())


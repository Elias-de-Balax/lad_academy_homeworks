"""
Звёздочка (множественное наследование и MRO). Создайте два миксина (TagMixin с add_tag(), Loggable с log()) и
класс Post(TagMixin, Loggable, Content) — миксины первыми, базовый класс последним. Напечатайте Post.__mro__ —
посмотрите порядок. Поэкспериментируйте: поменяйте порядок миксинов в объявлении класса и объясните, как изменится
результат выполнения (что победит при совпадении имён методов). Запишите вывод комментарием.
"""

from homework_14_task1_2 import Content

class Loggable:
    def log(self, message: str) -> str:
        return f"[LOG] {message}"

    def get_summary(self) -> str:
        return f"[LOG] {self.__class__.__name__}"

class TagMixin:
    def add_tag(self, tag: str) -> TagMixin:
        if not hasattr(self, "tags"):
            self.tags = []
        self.tags.append(tag)

        return self

    def get_summary(self) -> str:
        return f"[TAG] {self.__class__.__name__}"

class Post_V1(TagMixin, Loggable, Content):
    pass

class Post_V2(Loggable, TagMixin, Content):
    pass

class Post_V3(Content, TagMixin, Loggable):
    pass

post_v1 = Post_V1("Статья 1")
post_v1.add_tag("Python")
post_v2 = Post_V2("Статья 2")
post_v2.log("Пост создан")
post_v3 = Post_V3("Статья 3")
post_v3.add_tag("Django")
post_v3.log("Лог поста")

print(post_v1.get_summary())
print(post_v2.get_summary())
print(post_v3.get_summary())
print()
print(Post_V1.__mro__)
print(Post_V2.__mro__)
print(Post_V3.__mro__)

# Алгоритм разрешения методов (MRO) работает слева направо. Кто первый в списке наследования предоставил реализацию
# конкретного метода, тот и «побеждает», остальные методы других классов игнорируются
# В конце всегда стоит <class 'object'> - базовый класс всей иерархии классов python, у которого нет предка

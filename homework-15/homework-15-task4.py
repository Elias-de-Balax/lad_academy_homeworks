"""
Звёздочка: __eq__ + __hash__. Изучите, как переопределить __eq__ и __hash__ вместе (см. документацию Python по разделу
emulating hashable types). Сделайте так, чтобы Post сравнивался по заголовку (__eq__), а также мог быть ключом словаря
/ элементом множества (__hash__), согласованно: у равных объектов — равные hash. Проверьте: {post1, post2} не выбросит
TypeError: unhashable type, а два поста с одинаковым заголовком «склеятся» в один элемент множества.
"""
from dataclasses import dataclass

@dataclass
class Post:
    title: str
    content: str
    author: str

    def __eq__(self, other):
        if not isinstance(other, Post):
            return NotImplemented

        return self.title == other.title

    def __hash__(self):
        return hash(self.title)

    def __repr__(self):
        return f"Post(title={self.title})"


post1 = Post("title", "content", "author")
post2 = Post("title", "content_1", "author_1")
posts = {post1, post2}

print(post1 == post2)
print(posts)
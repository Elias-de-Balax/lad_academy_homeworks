from dataclasses import dataclass, field
from datetime import datetime

from blog_app.errors import DuplicateError

class PostMixin:
    _posts: list[Post] = field(default_factory=list)

    @property
    def posts(self) -> list[Post]:
        return self._posts.copy()

    #def add_post(self, post: Post) -> None:


@dataclass
class Author(PostMixin):
    id: int
    name: str
    _posts: list[Post] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("Имя автора не может быть пустым")

    @property
    def posts(self) -> list[Post]:
        return self._posts.copy()

    def add_post(self, post: Post) -> None:
        if post not in self._posts:
            post.author = self
            self._posts.append(post)


@dataclass
class Category:
    id: int
    title: str
    _posts: list[Post] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("Название категории не может быть пустым")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Category):
            return NotImplemented

        return self.title == other.title

    @property
    def posts(self) -> list[Post]:
        return self._posts.copy()

    def add_post(self, post: Post) -> None:
        if post not in self._posts:
            post.category = self
            self._posts.append(post)


@dataclass
class Tag:
    id: int
    title: str
    _posts: list[Post] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("Название тэга не может быть пустым")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented

        return self.title == other.title

    @property
    def posts(self) -> list[Post]:
        return self._posts.copy()

    def add_post(self, post: Post) -> None:
        if not post in self._posts:
            self._posts.append(post)


@dataclass
class Post:
    id: int
    title: str
    content: str
    author: Author
    category: Category
    _tags: list[Tag] = field(default_factory=list)
    created_at = datetime.now().strftime("%d.%m.%y %H:%M:%S")

    def __post_init__(self) -> None:
        if not self.title or not self.title.strip():
            raise ValueError("Заголовок статьи не может быть пустым")
        if not self.content or not self.content.strip():
            raise ValueError("Содержание статьи не может быть пустым")

    def __str__(self) -> str:
        return f"{self.title:20s} | {self.author.name:20s} | {self.category.title:20s}"

    @property
    def tag_titles(self) -> list[str]:
        return [tag.title for tag in self._tags]

    @property
    def tags(self) -> list[Tag]:
        return self._tags.copy()

    def add_tag(self, tag: Tag) -> None:
        if not tag in self._tags:
            self._tags.append(tag)
            tag.add_post(self)
        else:
            raise DuplicateError("Тэг уже в списке тэгов к статье")

if __name__ == "__main__":
    print(Post.__dict__)
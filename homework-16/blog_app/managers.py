import functools
import inspect
import json

from dataclasses import dataclass
from pathlib import Path
from typing import Self, Any
from unicodedata import category

from blog_app.errors import DuplicateError, ParameterNotFoundError, ValidationError
from blog_app.models import Author, Category, Tag, Post

# класс Blog создан по паттерну Синглтон с переопределением __new__ и __init__

@dataclass
class Blog:
    _instance = None
    _initialized = False

    _next_ids = {Author.__name__: 1,
                 Category.__name__: 1,
                 Tag.__name__: 1,
                 Post.__name__: 1}

    def __new__(cls, *args, **kwargs) -> Self | None:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False

        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return

        self._authors: list[Author] = []
        self._categories: list[Category] = []
        self._tags: list[Tag] = []
        self._posts: list[Post] = []

        self._initialized = True

    def _new_id(self, kind: str) -> int:
        new_id = self._next_ids[kind]
        self._next_ids[kind] += 1

        return new_id

    # Сделал для себя для понимания работы декоратора, проверяющего входные параметры функции
    @staticmethod
    def _check_params(rules: dict[str, list[dict[str, Any]]]):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # Извлекаем сигнатуру функции и связываем переданные аргументы с именами параметров функции
                bound_args = inspect.signature(func).bind(*args, **kwargs)

                for param_name, param_list in rules.items():
                    if param_name in bound_args.arguments:
                        for params in param_list:
                            if len(inspect.signature(params["predicate"]).parameters) > 1:
                                if params["predicate"](args[0], bound_args.arguments[param_name]):
                                    raise params["err_class"](params["err_text"])
                            else:
                                if params["predicate"](bound_args.arguments[param_name]):
                                    raise params["err_class"](params["err_text"])
                    else:
                        raise ParameterNotFoundError(f"Параметр {param_name} не найден")

                return func(*args, **kwargs)
            return wrapper
        return decorator

    @property
    def authors(self) -> list[Author]:
        return self._authors.copy()

    @property
    def categories(self) -> list[Category]:
        return self._categories.copy()

    @property
    def tags(self) -> list[Tag]:
        return self._tags.copy()

    @property
    def posts(self) -> list[Post]:
        return self._posts.copy()

    def add_author(self, name: str) -> Author:
        author_list = [author.name for author in self._authors]

        if not name in author_list:
            author = Author(self._new_id(Author.__name__), name)
            self._authors.append(author)
        else:
            author = self._authors[author_list.index(name)]

        return author

    def add_category(self, title: str) -> Category:
        category_list = [category.title for category in self._categories]

        if not title in category_list:
            category = Category(self._new_id(Category.__name__), title)
            self._categories.append(category)
        else:
            category = self._categories[category_list.index(title)]

        return category

    def add_tag(self, title: str) -> Tag:
        tag_list = [tag.title for tag in self._tags]

        if not title in tag_list:
            tag = Tag(self._new_id(Tag.__name__), title)
            self._tags.append(tag)
        else:
            tag = self._tags[tag_list.index(title)]

        return tag

    @_check_params({
        "author": [
            {"predicate": lambda author: not author, "err_class": ValidationError, "err_text": "Автор поста не определен"},
            {"predicate": lambda author: not type(author) is Author,
             "err_class": TypeError,
             "err_text": "Неподходящий тип данных автора поста"}],
        "category": [
            {"predicate": lambda category: not category,
             "err_class": ValidationError,
             "err_text": "Категория поста не определена"},
            {"predicate": lambda category: not type(category) is Category,
             "err_class": TypeError,
             "err_text": "Неподходящий тип категории поста"}]
    })
    def create_post(self,
                    title: str,
                    content: str,
                    author: Author,
                    category: Category) -> Post:
        post = Post(self._new_id(Post.__name__), title, content, author, category)

        author.add_post(post)
        category.add_post(post)
        self._posts.append(post)

        return post

    @_check_params({
        "tag": [
            {"predicate": lambda tag: not tag, "err_class": ValidationError, "err_text": "Тэг не определен"},
            {"predicate": lambda tag: not isinstance(tag, (Tag, str)),
             "err_class": TypeError,
             "err_text": "Неподходящий тип данных тэга"}],
        "post": [
            {"predicate": lambda post: not post, "err_class": ValidationError, "err_text": "Статья не определена"},
            {"predicate": lambda post: not type(post) is Post,
             "err_class": TypeError,
             "err_text": "Неподходящий тип данных статьи"}]
    })
    def add_tag_to_post(self, post: Post, tag: Tag | str) -> bool:
        if type(tag) is str:
            tag = self.add_tag(tag)

        try:
            post.add_tag(tag)
        except DuplicateError:
            return False
        else:
            return True

    @_check_params({
        "tag": [
            {"predicate": lambda tag: not tag, "err_class": ValidationError, "err_text": "Тэг не определен"},
            {"predicate": lambda tag: not isinstance(tag, (Tag, str)),
             "err_class": TypeError,
             "err_text": "Неподходящий тип данных тэга"}]
    })
    def posts_by_tag(self, tag: Tag | str) -> list[Post]:
        filter_func = lambda post: tag in post.tags

        if type(tag) is str:
            filter_func = lambda post: tag in post.tag_titles

        return list(filter(filter_func, self._posts))

    @_check_params({
        "category": [
            {"predicate": lambda category: not category,
             "err_class": ValidationError,
             "err_text": "Категория не определена"},
            {"predicate": lambda category: not type(category) is Category,
             "err_class": TypeError,
             "err_text": "Неподходящий тип данных категории"}]
    })
    def posts_by_category(self, category: Category) -> list[Post]:
        return list(filter(lambda post: category == post.category, self._posts))

    def find_posts(self, text: str) -> list[Post]:
        return list(
            filter(lambda post: text.lower() in (post.title+" "+post.content).lower(), self._posts)
        )

    @classmethod
    def load(cls, arg_file: Path) -> Blog:
        if not arg_file.exists():
            return cls()

        with open(arg_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        authors = {a["id"]: Author(a["id"], a["name"]) for a in data["authors"]}
        categories = {c["id"]: Category(c["id"], c["title"]) for c in data["categories"]}
        tags = {t["id"]: Tag(t["id"], t["title"]) for t in data["tags"]}

        blog = cls()
        blog._authors = list(authors.values())
        blog._categories = list(categories.values())
        blog._tags = list(tags.values())

        for post_data in data["posts"]:
            post = Post(
                post_data["id"],
                post_data["title"],
                post_data["content"],
                authors[post_data["author_id"]],
                categories[post_data["category_id"]]
            )
            authors[post_data["author_id"]].add_post(post)
            categories[post_data["category_id"]].add_post(post)
            for tag_id in post_data["tag_ids"]:
                post.add_tag(tags[tag_id])

            blog._posts.append(post)

        blog._next_ids = {
            Author.__name__: max([a.id for a in blog._authors], default=0) + 1,
            Category.__name__: max([c.id for c in blog._categories], default=0) + 1,
            Tag.__name__: max([t.id for t in blog._tags], default=0) + 1,
            Post.__name__: max([p.id for p in blog._posts], default=0) + 1,
        }

        return blog

    def _post_to_dict(self, post: Post) -> dict:
        return {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author_id": post.author.id,
            "category_id": post.category.id,
            "tag_ids": [tag.id for tag in post.tags],
            "created_at": post.created_at,
        }

    def save(self, arg_file: Path) -> None:
        data = {
            "authors": [{"id": a.id, "name": a.name} for a in self._authors],
            "categories": [{"id": c.id, "title": c.title} for c in self._categories],
            "tags": [{"id": t.id, "title": t.title} for t in self._tags],
            "posts": [self._post_to_dict(post) for post in self._posts],
        }

        with open(arg_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
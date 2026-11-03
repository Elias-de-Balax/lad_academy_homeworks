"""
Мини-проект «Блог CLI» — причесать. Взять классы Post/Author/Category из Этапа 4 и добавить: (а) статический метод
Post.is_valid_text(text) (текст не пустой), (б) метод класса Author.from_csv(line) (разбирает строку имя;email),
(в) возможность вывести только посты одной категории.
"""

class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def from_csv(cls, line):
        name, email = line.split(";")

        return cls(name, email)

class Category:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

class Post:
    def __init__(self, title, text, author, category):
        self.title = title
        self.text = text
        self.author = author
        self.category = category

    def display(self):
        print(f"{self.title:25s} | {self.category.title:25s} | автор: {self.author.name:25s}")

    @staticmethod
    def is_valid_text(text) -> bool:
        return isinstance(text, str) and bool(text.strip())

posts = [
    Post("Введение в Django",
         "Введение в Django",
         Author.from_csv("Василий;example@gmail.com"),
         Category("Django")),
    Post("Списки в Python",
         "Списки в Python",
         Author.from_csv("Сергей;mail@yandex.ru"),
         Category("Python")),
    Post("Как установить uv",
         "Как установить uv",
         Author.from_csv("Иван;mail@gmail.com"),
         Category("Инструментарий")),
    Post("Применение Django в Web",
         "Применение Django в Web",
         Author.from_csv("Петр;example@mail.ru"),
         Category("Django"))
]

def add_post():
    title = input("Заголовок: ")
    text = input("Текст: ")
    author_name = input("Имя автора: ")
    author_email = input("Email автора: ")
    category_title = input("Категория: ")

    if (Post.is_valid_text(title)
        and Post.is_valid_text(text)
        and Post.is_valid_text(author_name)
        and Post.is_valid_text(author_email)
        and Post.is_valid_text(category_title)
    ):
        author = Author(author_name, author_email)
        category = Category(category_title)
        post = Post(title, text, author, category)
        posts.append(post)

        print("Пост добавлен.\n")
    else:
        print("Были введены пустые строки.")

def show_posts():
    category_title = input("Категория: ").strip().lower()

    if Post.is_valid_text(category_title):
        category = Category(category_title)
        # как вариант, сравнивать экземпляры класса благодаря __eq__
        find_posts = filter(lambda post: post.category == category, posts)

        if not find_posts:
            print("Постов пока нет.\n")
            return

        for post in find_posts:
            post.display()
    else:
        print("Не задана категория.")

while True:
    action = input("Действие (add / show / exit): ").strip().lower()

    match action:
        case "add":
            add_post()
        case "show":
            show_posts()
        case "exit":
            break
        case _:
            print("Неизвестное действие.\n")
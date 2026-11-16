class Author:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Автор: {self.name}"

    def __repr__(self):
        return f"Author(name={self.name!r}, email={self.email!r})"


class Post:
    def __init__(self, title: str, content: str, author: Author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Название: {self.title:25s} | {self.author}"

    def __repr__(self):
        return f"Post(title={self.title!r}, author={self.author!r})"


class Category:
    def __init__(self, name: str):
        self.name = name
        self.posts = []

    def __str__(self):
        temp_str = ""

        for post in self.posts:
            temp_str += f"\n{post}"

        return f"Категория «{self.name}»: {temp_str}"

    def __repr__(self):
        return f"Category(name={self.name!r}, posts={self.posts!r})"

    def append(self, post: Post) -> None:
        self.posts.append(post)

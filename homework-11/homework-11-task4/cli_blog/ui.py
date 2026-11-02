import json

from rich.console import Console
from rich.table import Table
from cli_blog import data

console = Console()

def create_post_menu() -> None:
    title = input("Название статьи: ")
    author = input("Автор: ")
    text = input("Текст статьи: ")

    data.create_post(title, author, text)

    console.print(f"[green]Статья «{title}» сохранена.[/green]")

def show_posts_menu() -> None:
    posts = data.list_posts()
    if not posts:
        console.print("[yellow]Статей пока нет.[/yellow]")
        return

    table = Table(title="Статьи блога")
    table.add_column("Название")
    table.add_column("Автор")
    table.add_column("Текст")

    for post in posts:
        table.add_row(post["title"], post["author"], post["text"])

    console.print(table)

def find_post() -> None:
    title = input("Название(часть названия) статьи для поиска: ")

    post = data.find_post(title)
    if not post:
        console.print("[red]Статья не найдена.[/red]")
        return

    table = Table(title="Найденная статья")
    table.add_column("Название")
    table.add_column("Автор")
    table.add_column("Текст")

    table.add_row(post["title"], post["author"], post["text"])

    console.print(table)

def load_posts(arg_file) -> None:
    if arg_file.exists():
        with open(arg_file, "r", encoding="utf-8") as f:
            data._posts = json.load(f)

def save_posts(arg_file) -> None:
    if data._posts:
        with open(arg_file, "w", encoding="utf-8") as f:
            json.dump(data._posts, f, ensure_ascii=False, indent=2)

# На всякий случай: Прямой доступ к data._posts лучше всего делать через get\set в рамках ООП
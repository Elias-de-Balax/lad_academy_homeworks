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


"""Собери мини-проект «Блог CLI» из модулей. Создай пакет с модулями data.py (хранит статьи — список словарей с title,
    author, text, а также функции create_post, list_posts, find_post) и ui.py (запрашивает данные, выводит список через
    rich). Добавь main.py с меню и if __name__ == "__main__":. Убедись, что можно добавить статью, показать список и
    найти статью по названию."""

from cli_blog import ui

def main():
    while True:
        print()
        print("Меню:")
        print("1. Добавить статью")
        print("2. Показать статьи")
        print("3. Найти статью")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        match choice:
            case "1":
                ui.create_post_menu()
            case "2":
                ui.show_posts_menu()
            case "3":
                ui.find_post()
            case "0":
                print("Работа завершена.")
                break
            case _:
                print("Неизвестная команда.")

if __name__ == "__main__":
    main()
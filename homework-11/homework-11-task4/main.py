"""
«Блог CLI» (мини-проект). Доработать утилиту blog_cli.py: добавить сохранение нескольких полей статьи (заголовок, автор,
содержание) и вывод красиво отформатированного списка статей при каждом запуске. Проверить, что данные переживают
перезапуск программы.
"""

from pathlib import Path
from cli_blog import ui

def main():
    print("Запуск программы из", Path.cwd())
    data_file = Path("cli_blog.json")
    ui.load_posts(data_file)

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
                ui.save_posts(data_file)

                print("Работа завершена.")
                break
            case _:
                print("Неизвестная команда.")

if __name__ == "__main__":
    main()

"""
Звёздочка (работа с путями, pathlib). Переписать программу из задачи 4 так, чтобы файл статьи сохранялся в подпапке
проекта. Например, создайте папку data/ через Path("data").mkdir(exist_ok=True) и сохраняйте data/articles.json.
Убедитесь, что при запуске из любой папки программа находит свой файл. Используйте Path.cwd() для понимания, откуда
запускается скрипт.
"""

from pathlib import Path
from cli_blog import ui

def main():
    print("Запуск программы из", Path.cwd())

    Path("data").mkdir(exist_ok=True)
    data_file = Path("data/cli_blog.json")
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

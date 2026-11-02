"""
Свои исключения в «Блог CLI». Расширьте утилиту блога: добавьте class PostNotFoundError(Exception) и функцию
get_post(index), которая возвращает пост по номеру; если такого поста нет — бросает PostNotFoundError. В сценарии list
обработайте её так, чтобы пользователь видел «Пост № N не найден». Убедитесь, что чужие ошибки (например, IndexError)
не попадают в этот обработчик.
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
        print("4. Вывести статью по её номеру")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        match choice:
            case "1":
                ui.create_post_menu()
            case "2":
                ui.show_posts_menu()
            case "3":
                ui.find_post()
            case "4":
                ui.get_post()
            case "0":
                ui.save_posts(data_file)

                print("Работа завершена.")
                break
            case _:
                print("Неизвестная команда.")

if __name__ == "__main__":
    main()

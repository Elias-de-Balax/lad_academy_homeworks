"""Звёздочка (относительные импорты и пакет): внутри пакета blog используй относительные импорты (from . import data),
    а не абсолютные (from blog import data). Объясни в комментарии, в чём разница, и покажи, что при запуске python
    blog/ui.py такие импорты «падают», а при запуске main.py из корня — работают. Подсказка: попробуй и так, и так —
    это и есть главный вывод."""

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
    main() # При любом импорте в ui.py from . (или cli_blog) import data не упадет
           # тк main.py считается верхнеуровневым скриптом и он "видит" пакет
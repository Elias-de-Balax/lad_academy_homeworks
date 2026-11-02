"""
Звёздочка (логирование). Замените все print() в утилите блога на логирование через logging: INFO для «обычных» событий,
WARNING для предупреждений, ERROR для ошибок. Настройте basicConfig с форматом %(asctime)s | %(levelname)s | %(message)s.
Добейтесь, чтобы при «обычной» работе выводились только INFO, а при сбое — ERROR в журнал. Объясните в комментарии,
зачем logging лучше print()
"""

import sys
import logging

from pathlib import Path
from cli_blog import ui

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def main():
    logging.info("Запуск программы из %s", Path.cwd())

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

                logging.info("Работа завершена.")
                break
            case _:
                logging.warning("Неизвестная команда.")

if __name__ == "__main__":
    main()

# print выводит данные только в консоль, а logging может кроме консоли вывести в файл, память, сетевые сервисы
# те возможностей у logging вывести информацию пользователю больше
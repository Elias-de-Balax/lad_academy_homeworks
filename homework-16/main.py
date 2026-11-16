"""
1. Поиск по тегу и по тексту. Добавьте в Blog метод posts_by_tag(tag) (он уже есть — расширьте вывод в main.py так,
чтобы выводить посты по введённому тегу) и метод find_posts(text), который возвращает посты, где text встречается в
заголовке или тексте. Выведите результат в консоль.
2. Уникальность и валидация. Сделайте модель устойчивой: add_author/add_category/add_tag должны бросать ValueError,
если объект с таким именем/названием уже есть; create_post должен бросать ValueError, если title пустой или если
author/category переданы как None. Подсказка: это пересекается с занятием 12 (обработка исключений) — используйте raise
ValueError(...) с понятным сообщением и обработайте его в main.py.
3. Интерактивное меню CLI. Превратите main.py в настоящую утилиту с циклом команд: add-author, add-category, add-tag,
create-post, add-tag-to-post, show, search <категория>, save, load, quit. Например, команда create-post запрашивает
заголовок, текст, автора и категорию по имени. Подсказка: считывайте строку через input(), разбивайте через split(), а
неизвестную команду — просто сообщайте об этом.
4. ⭐ Усложнить связи многие-ко-многим (теги). Сделайте Blog.add_tag_to_post(post, tag) возвращающим True, если тег был
добавлен, и False, если такой тег у поста уже есть (без создания дубликата).
"""

from pathlib import Path

from blog_app.managers import Blog
from blog_app.models import Post

def create_post(blog: Blog) -> None:
    data = input("Добавьте статью в формате \"Заголовок;Текст;Автор;Категория\": ").split(";")

    try:
        author = blog.add_author(data[2])
        category = blog.add_category(data[3])
        blog.create_post(data[0], data[1], author, category)
    except IndexError:
        print(f"Ошибка: Статья задана в неверном формате")
    else:
        print("Статья добавлена в список успешно")

def add_objects(blog: Blog) -> None:
    print("\nПодменю:")
    print("1. Добавить автора")
    print("2. Добавить категорию")
    print("3. Добавить тэг")
    print("0. Выход из подменю")

    while True:
        try:
            match input("\nВыберите действие в подменю: "):
                case "1":
                   blog.add_author(input("Введите автора: "))
                case "2":
                    blog.add_category(input("Введите категорию: "))
                case "3":
                    blog.add_tag(input("Введите тэг: "))
                case "0":
                    break
                case _:
                    print("Неизвестная команда.")
                    continue
        except Exception as e:
            print(f"Ошибка: {e}")
        else:
            print("Данные добавлены в список успешно")

def show_posts(posts: list[Post]) -> None:
    if len(posts) > 0:
        print("\nСписок статей:")

        for i, post in enumerate(posts, start=1):
            print(f"{i}. {post} | тэги: {post.tag_titles}")
    else:
        print("Нет статей для вывода")

def find_posts(blog: Blog) -> None:
    print("\nПодменю:")
    print("1. Поиск по заголовку/содержанию")
    print("2. Поиск по тэгу")
    print("3. Поиск по автору")
    print("4. Поиск по категории")
    print("0. Выход из подменю")

    while True:
        try:
            match input("\nВыберите действие в подменю: "):
                case "1":
                    show_posts(blog.find_posts(input("Введите строку для поиска статьи: ")))
                case "2":
                    show_posts(blog.posts_by_tag(input("Введите тэг для поиска статьи: ")))
                case "3":
                    show_posts(blog.posts_by_author(input("Введите автора для поиска статьи: ")))
                case "4":
                    show_posts(blog.posts_by_category(input("Введите категорию для поиска статьи: ")))
                case "0":
                    break
                case _:
                    print("Неизвестная команда.")
        except Exception as e:
            print(f"Ошибка: {e}")

def bind_tags_to_post(blog: Blog) -> None:
    if tag_name := input("Введите имя тэга: "):
        show_posts(blog.posts)

        try:
            post_num = int(input("\nВведите номер статьи, которой необходимо присвоить тэг: "))

            print(f"Тэг \"{tag_name}\" "
                  f"{"присвоен статье" if blog.add_tag_to_post(blog.posts[post_num-1], tag_name) else "уже есть у статьи"}"
                  f" под номером {post_num}")
        except ValueError, IndexError:
            print("Неверно указан номер статьи")
    else:
        print("Тэг не определен")

def main() -> None:
    Path("data").mkdir(exist_ok=True)
    data_file = Path("data/blog.json")
    blog = Blog.load(data_file)

    while True:
        print("\nМеню:")
        print("1. Добавить статью")
        print("2. Добавить Автора/Категорию/Тэг")
        print("3. Привязать тэги к статье")
        print("4. Показать статьи")
        print("5. Поиск статьи")
        print("0. Выход")

        try:
            match input("\nВыберите действие в главном меню: "):
                case "1":
                    create_post(blog)
                case "2":
                    add_objects(blog)
                case "3":
                    bind_tags_to_post(blog)
                case "4":
                    show_posts(blog.posts)
                case "5":
                    find_posts(blog)
                case "0":
                    blog.save(data_file)

                    print("Работа завершена.")
                    break
                case _:
                    print("Неизвестная команда.")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == '__main__':
    main()
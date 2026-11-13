from pathlib import Path

from blog_app.managers import Blog

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
    print()
    print("Подменю:")
    print("1. Добавить автора")
    print("2. Добавить категорию")
    print("3. Добавить тэг")
    print("0. Выход из подменю")

    while True:
        choice = input("\nВыберите действие в подменю: ")

        try:
            match choice:
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

def find_posts(blog: Blog) -> None:
    pass

def bind_tags_to_post(blog: Blog) -> None:
    pass

def show_posts(blog: Blog) -> None:
    pass

def main() -> None:
    Path("data").mkdir(exist_ok=True)
    data_file = Path("data/blog.json")
    blog = Blog.load(data_file)

    print("Меню:")
    print("1. Добавить статью")
    print("2. Добавить Автора/Категорию/Тэг")
    print("3. Привязать тэги к статье")
    print("4. Показать статьи")
    print("5. Найти статью по заголовку/тексту, либо по тэгу")
    print("0. Выход")

    while True:
        choice = input("\nВыберите действие в главном меню: ")

        try:
            match choice:
                case "1":
                    create_post(blog)
                case "2":
                    add_objects(blog)
                case "3":
                    bind_tags_to_post(blog)
                case "4":
                    show_posts(blog)
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
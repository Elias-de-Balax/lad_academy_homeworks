"""Меню блога (список постов). Заведите список постов — каждый пост это список [дата, заголовок, категория]
   (дата в формате ГГГГ-ММ-ДД). Выведите все посты, отсортируйте их по дате, а затем отфильтруйте по введённой с
   клавиатуры категории. Если в этой категории постов нет — выведите сообщение об этом."""

input_posts = [
    ["2026-02-18", "Как установить uv", "Инструментарий"],
    ["2026-02-22", "Списки в Python", "Python"],
    ["2026-02-10", "Введение в Django", "Django"],
    ["2026-02-25", "Применение Django в Web", "Django"]
]

while True:
    print("\nЧто делаем?")
    print("1 — показать все посты")
    print("2 — отсортировать по дате")
    print("3 — отфильтровать по категории")
    print("0 — выйти")

    choice = input("Ваш выбор: ")

    match choice:
        case "1":
            print("\nВсе посты:")
            for post in input_posts:
                print(f"{post[0]}  |  {post[1]:25s}  |  {post[2]:20s}|")
        case "2":
            input_posts.sort()

            print("\nОтсортировано по дате:")
            for post in input_posts:
                print(f"{post[0]}  |  {post[1]:25s}  |  {post[2]:20s}|")
        case "3":
            target = input("Введите категорию: ")
            filtered = [post for post in input_posts if post[2].lower() == target.lower()]

            if filtered:
                print(f"\nПосты в категории «{target}»:")

                for post in filtered:
                    print(f"{post[0]}  |  {post[1]:25s}  |  {post[2]:20s}|")
            else:
                print(f"Постов в категории «{target}» нет.")
        case "0":
            print("До свидания!")
            break
        case _:
            print("Попробуйте ещё раз.")

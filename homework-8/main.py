"""Функции создания и вывода. Реализуйте create_article(...) (добавляет статью) и show_articles(...) (выводит все статьи
    по красивому шаблону). Программа должна уметь добавлять статью и показывать весь список. (Совет: добавьте в статью
    поле views — число просмотров.)
    Фильтрация и поиск. Реализуйте filter_by_category(articles, category) и find_articles(articles, query) (частичный
    поиск по заголовку/автору, регистронезависимо). Выведите результат в читаемом виде.
    Сортировка по полю. Реализуйте sort_articles(articles, key=..., reverse=False), где key — «title», «author»,
    «category», «rating» или «views». Продемонстрируйте сортировку по рейтингу и по числу просмотров (по убыванию).
    Обработка неверного ввода. В функциях создания/сортировки добавьте проверки: рейтинг должен быть числом, поле
    key — допустимым; при ошибке выводите понятное сообщение, не «падайте». (Подсказка: пригодится try/except из темы
    «Ошибки» или проверка через in.)
    (со звёздочкой). Дополните sort_articles так, чтобы она принимала kwargs (например, sort_articles(articles,
    key="rating", reverse=True, bonus="views")) и умела сортировать по нескольким полям**: сначала по key, а при
    равенстве — по bonus. Используйте key=lambda a: (a[key], a.get(bonus, 0)) — объясните, почему кортеж из двух полей
    решает задачу вторичной сортировки.
    (со звёздочкой, продвинутая). Коротко изучите по документации модуль functools (функции lru_cache, partial, wraps)
    или базовое понятие рекурсии (функция, вызывающая саму себя, например, факториал или поиск по вложенному списку).
    Опишите своими словами комментарием в коде, что вы выбрали и зачем, и приведите рабочий пример. Важно: декораторы
    полноценно разбираются на занятии 9 — сейчас просто «познакомьтесь» и зафиксируйте наблюдение.
"""

array_articles = [["Как установить uv", "", "Инструментарий", 4.8, 30],
                  ["Списки в Python", "Владимир Дронов", "Python", 5, 10],
                  ["Введение в Django", "Гарри Персиваль", "Django", 4.8, 20],
                  ["Применение Django в Web", "Арун Равиндран", "Django", 4.6, 20],
                  ["Введение в FastAPI", "Себастьян Рамирес", "FastAPI", 4.9, "15"]]
articles = []

def create_article(title, author, category, rating, views):
    if (not type(views) is int
        or not type(rating) in (float, int)):
        raise TypeError(f"Заголовок \"{title}\": Неверно заданы числовые значения у рейтинга/просмотров")

    article = {
        'title': title,
        'author': author,
        'category': category,
        'rating': rating,
        'views': views
    }
    return article

def show_articles(article_list):
    if not article_list:
        print("Список статей пуст")
        return

    for i, article in enumerate(article_list, start=1):
        print(f"{i}. {article['title']} — "
              f"автор: {article['author'] if len(article['author']) else "Неизвестный автор"}, "
              f"категория: {article['category']}, "
              f"рейтинг {article['rating']}, "
              f"просмотры: {article['views']}")

def filter_by_category(article_list, category) -> list:
    return [article for article in article_list if article["category"].lower() == category.lower()]

def find_articles(article_list, query) -> list:
    if query:
        return [article for article in article_list
                    #if ((-1 != article["title"].lower().find(query.lower()))
                    #    or (-1 != article["author"].lower().find(query.lower())))] # Что-то громоздко...
                    if query.lower() in (article["title"] + article["author"]).lower()] # ????
    else:
        return None

def sort_articles(article_list, key="rating", reverse=True) -> list:
    if key.lower() in ["title", "author", "category", "rating", "views"]:
        return sorted(article_list, key=lambda a: a[key.lower()], reverse=reverse)
    else:
        raise TypeError("Неверно задано поле для сортировки.")

def sort_articles_ex(article_list, **kwargs) -> list:
    key = kwargs.get("key", "rating")
    bonus = kwargs.get("bonus", "views")
    reverse = kwargs.get("reverse", True)

    if key.lower() in ["title", "author", "category", "rating", "views"]:
        # Python сортирует по правилам лексикографического сравнения кортежей
        # Сначала сортируются первые элементы, если они равны, то вторые
        return sorted(article_list, key=lambda a: (a[key], a.get(bonus, 0)), reverse=reverse)
    else:
        raise TypeError("Неверно задано поле для сортировки.")

for article in array_articles:
    try:
        articles.append(create_article(*article))
    except TypeError as e:
        print(e.__str__())

while True:
    print("\nЧто делаем?")
    print("1 — показать все статьи")
    print("2 — отфильтровать по категории")
    print("3 - поиск по заголовку/автору")
    print("4 - сортировка по определеннному полю")
    print("5 - расширенная сортировка по двум полям")
    print("0 — выйти")

    choice = input("Ваш выбор: ")

    match choice:
        case "1":
            print("\nИсходный список: ")
            show_articles(articles)
        case "2":
            target = input("Введите категорию: ")

            print("\nОтфильтрованный список")
            show_articles(filter_by_category(articles, target))
        case "3":
            find_keyword = input("Задайте слово(часть слова) для поиска: ")

            print("Найденные статьи:")
            show_articles(find_articles(articles, find_keyword))
        case "4":
            sort_keyword = input("Задайте поле для сортировки (title/author/category/rating/views): ")

            try:
                print(f"Сортировка по {sort_keyword}:")
                show_articles(sort_articles(articles, key=sort_keyword))
            except TypeError as e:
                print(e.__str__())
        case "5":
            show_articles(sort_articles_ex(articles, key="rating", reverse=True, bonus="views"))
        case "0":
            print("До свидания!")
            break
        case _:
            print("Попробуйте ещё раз.")
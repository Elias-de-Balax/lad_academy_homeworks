"""Один декоратор — на несколько функций. Напишите декоратор @logged (или @time_it) и примените его сразу к трём
    функциям «блога»: create_article, get_article_by_id, delete_article. Заготовки функций сделайте простыми (работа с
    тем же списком статей в памяти), чтобы поведение добавлял именно декоратор. Поясните комментарием, что изменилось
    бы, если бы пришлось вставлять логирование в тело каждой функции вручную."""

from collections import defaultdict
from homework_9_task2 import logged, time_it

articles = defaultdict(list)

@logged
@time_it
def create_article(title, category):
    article = {
        'title': title,
        'category': category
    }
    return article

@logged
def get_article_by_id(arg_dict, article_id):
    return arg_dict.get(article_id)

@logged
def delete_article(arg_dict, article_id):
    arg_dict.pop(article_id, None)

articles[0].append(create_article("Списки в Python", "Python"))
articles[1].append(create_article("Введение в Django", "Django"))

print("Исходный список:\n", dict(articles))
print()
print("\nНайденный словарь:", get_article_by_id(articles, 1))
print()
delete_article(articles, 1)
print("Обновленный список:\n", dict(articles))

# Eсли бы пришлось вставлять логгирование в тело каждой функции вручную, пришлось бы писать много лишнего
# повторяющегося кода с потенциальной вероятностью ошибок и захламления основного кода функций
"""
Самостоятельное изучение юнит-тесты. Напишите файл tests_blog.py с проверками через простые assert (без сторонних
тест-библиотек): создайте данные, сохраните в JSON, загрузите и проверьте, что автор поста, категория и теги не
потерялись. Важно: и категорию (cat), и автора берите из загруженного блога, например: cat = next(c for c in
loaded.categories if c.title == "Backend"), затем assert loaded.posts_by_category(cat)[0].author.name == "Иван Петров".
Запускайте через uv run python tests_blog.py.
"""

from pathlib import Path

from blog_app.managers import Blog

def test():
    Path("data").mkdir(exist_ok=True)
    data_file = Path("data/test_blog.json")

    blog = Blog()
    post = blog.create_post(
        "Заголовок", "Контент", blog.add_author("Иван Петров"), blog.add_category("Backend")
    )
    post.add_tag(blog.add_tag("Python"))
    post.add_tag(blog.add_tag("Django"))
    blog.save(data_file)

    loaded = Blog.load(data_file)
    cat = next(c for c in loaded.categories if c.title == "Backend")
    assert loaded.posts_by_category(cat)[0].author.name == "Иван Петров", "Автор поста не найден"

    try:
        assert loaded.posts_by_category(cat)[0].author.name == "Василий Петров", "Автор поста не найден"
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    test()
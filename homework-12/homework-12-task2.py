"""
Безопасное чтение постов. Напишите функцию load_posts, которая читает JSON-файл постов и: возвращает пустой список,
если файла нет (FileNotFoundError); при битом JSON (json.JSONDecodeError) — логирует ошибку и пробрасывает исключение
raise (не «притворяясь», что всё хорошо). Подсказка: используйте logging и Path.
"""

import json
import logging

from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

posts_file = Path("posts.json")

def load_posts(path) -> list:
    try:
        with open(path, "r", encoding="utf-8") as f:
            posts = json.load(f)
    except FileNotFoundError:
        logging.error("Файл не найден.")

        return []
    except json.JSONDecodeError as e:
        logging.error("Битый файл. %s", e)

        raise
    else:
        logging.info(f"Прочитано записей из файла: {len(posts)}")

        return posts
    finally:
        logging.info("Загрузка файла завершена.")

try:
    posts = load_posts(posts_file)
except Exception as e:
    logging.error("Поймана ошибка %s", e.__class__.__name__)
"""
3. Реализовать контекстный менеджер для транзакции. Сделайте через @contextmanager менеджер, который перед yield
открывает «журнал изменений» (например, пишет в файл operations.log «Начало…»), а после yield — «Конец…», и
гарантированно это делает даже при ошибке. Покажите, что запись происходит в любом случае.
"""

from contextlib import contextmanager

LOG_FILE = "operations.log"

class TransactionError(Exception):
    pass


@contextmanager
def transaction(log_path: str = LOG_FILE):
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("Начало транзакции\n")

    try:
        yield
    except Exception as e:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write("Ошибка в транзакции\n")
        raise TransactionError(e)
    finally:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write("Конец транзакции\n")


with transaction():
    print("Действия в транзакции...")
    print("Транзакция заканчивается хорошо...")

try:
    with transaction():
        print("\nДействия в транзакции...")
        raise ValueError("В транзакции что-то пошло не так")
except TransactionError as e:
    print(f"Перехвачено исключение: {e}")

print("\nСодержимое log-файла:")
with open(LOG_FILE, "r", encoding="utf-8") as f:
    print(f.read())
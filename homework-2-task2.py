"""Проверка доступа к посту. Создайте данные поста (флаг is_published, признак is_premium, строку text) и
   решите через and/or/not, показывать ли его: пост виден, если он опубликован и (не премиум или у пользователя
   есть подписка). Выведите решение. Подсказка: используйте скобки в сложном условии. Добавьте проверку на «истинность»
   text — пустой текст не показывается."""

text = "Hello World!"

is_premium = True
is_published = True
has_subscription = True

if not bool(text):
    print("Поста нет.")
else:
    if is_published and (not is_premium or has_subscription):
        print(f"Текст поста: {text}")
    else:
        print("Пост скрыт, либо нет подписки на пост.")



"""Звёздочка (валидация телефона/email). Написать проверку корректности e-mail без регулярных выражений, только методами
   строк: есть ровно один @, слева и справа от него есть непробельные символы, в доменной части есть точка, домен
   заканчивается на 2+ буквы (endswith + проверка isalpha на суффиксе). Дополнительно — проверить номер телефона в
   формате +7-XXX-XXX-XX-XX: разбить по - на 5 частей, первая равна +7, остальные — isdigit() и нужной длины (len).
   Вывести True/False для нескольких примеров."""

emails = ["alex_dev_2026@yandex.ru",
          "a.b.c@a.b.c.ru",
          ".ivan.petrov@gmail.com",
          "user@@example.com",
          "user-name@my-site.io"]

phones = ["+7-999-123-12-22",
          "7-999-123-12-22",
          "+7-9991231222",
          "+7-999a123-12-22",
          "+7-999--123-1222"]

"""
Локальная часть (до @)
Длина: не более 64 символов.
Допустимые символы: латинские буквы a–z, A–Z, цифры 0–9, а также . (точка), - (дефис), _ (подчёркивание), + (плюс).
Ограничения для точки: нельзя ставить в начале или в конце, нельзя использовать две точки подряд (..).
Запрещены: пробелы, любые спецсимволы вне разрешённого списка (например, !, %, /, \\, (, ), кавычки и т.п.).
Регистр: технически не важен, но принято писать строчными.
Символ @ должен быть ровно один.
Не должно быть пробелов рядом с ним.

Доменная часть (после @)
Состоит из меток (поддомен/домен), разделённых точками.
Каждая метка: только латинские буквы, цифры и дефисы; не может начинаться или заканчиваться дефисом.
В конце — домен верхнего уровня (TLD), например .com, .ru, .org.
Длина всего адреса: не более 254 символов.
"""

def is_validated_email(email_: str) -> bool:
    # Проверяем на первичные признаки корректности
    if (not len(email_)
        or (254 < len(email_))
        or (1 != email_.count("@"))
        or ".." in email_
        ):
        return False

    special_chars = "-.+_"
    name, domain = email_.split("@")

    # Проверяем на наличие строки, длину не более 64 символов, вхождение спецсимволов в начале и в конце строки
    if (not len(name)
        or (64 < len(name))
        or name[0] in special_chars
        or name[-1] in special_chars
        ):
        return False

    if (not len(domain)
        or domain[0] in special_chars
        or domain[-1] in special_chars
        ):
        return False

    allowed_domain = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
    allowed_name = allowed_domain + special_chars[1:]

    # Осуществляем проверку на вхождение в список разрешенных символов
    for char in name:
        if char not in allowed_name:
            return False

    # Разбиваем домен на поддомены по точкам
    sub_domains = domain.split(".")

    # Проверяем на наличие не менее 2 частей домена и наличие только букв в домене верхнего уровня (не менее 2х)
    if ((2 > len(sub_domains))
        or (2 > len(sub_domains[-1]))
        or not sub_domains[-1].isalpha()
        ):
        return False

    # Проверка на дефисы в начале и конце поддомена
    for sub_domain in sub_domains[:-1]:
        if (not len(sub_domain) # Возможно, это лишнее после всех проверок выше, но подстраховываюсь
            or sub_domain.startswith("-")
            or sub_domain.endswith("-")
            ):
            return False

        for char in sub_domain:
            if char not in allowed_domain:
                return False

    return True

def is_validated_phone(phone_: str) -> bool:
    try:
        # формат +7-XXX-XXX-XX-XX
        # Проверяем на первичные признаки корректности
        if ((16 != len(phone_))
            or (4 != phone_.count("-"))
            or not phone_.startswith("+7-")
            ):
            raise ValueError

        # Проверяем на числовые значения 4 блока цифр
        if (not phone_[3:6].isdigit()
            or not phone_[7:10].isdigit()
            or not phone_[11:13].isdigit()
            or not phone_[14:15].isdigit()
            ):
            raise ValueError

        return True
    except ValueError:
        return False

for email in emails:
    print(f"Email {email} {"" if is_validated_email(email.strip()) else "не"}корректный")

print()

for phone in phones:
    print(f"Телефон {phone} {"" if is_validated_phone(phone.strip()) else "не"}корректный")
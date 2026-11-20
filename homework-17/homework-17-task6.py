"""
6. Звёздочка (самостоятельное изучение). Возьмите реальный пример типизации из документации Django Ninja или Pydantic
(схема, list[Post], Optional) и прокомментируйте в коде, как аннотации превращаются в валидацию и документацию API.
"""
# Взято из https://django-ninja.dev/guide/schemas/

from django.contrib.auth.models import User
from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserIn(Schema):
    username: str
    password: str


class UserOut(Schema):
    id: int
    username: str


@api.post("/users", response=UserOut)
def create_user(request, data: UserIn):
    return User.objects.create_user(data.username, password=data.password)

# Django Ninja использует UserOut для проверки и сериализации возвращаемых create_user данных. Это означает, что ответ
# ограничивается полями, объявленными в UserOut, даже если возвращаемый объект имеет другие атрибуты.
# Django Ninja на основании описаний аннотаций самостоятельно формирует документацию API в формате OpenAPI (Swagger)


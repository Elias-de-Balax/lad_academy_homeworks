"""4. Множества: уникальные значения. Дан список тегов tags (с дублями). Составьте множество уникальных тегов через set,
    затем: проверьте, есть ли в нём конкретный тег через in; добавьте новый тег через add; удалите несуществующий тег
    через discard (без ошибки) и через remove в try/except — запишите, чем они отличаются, в комментарии."""

tags_list = ["uv", "python", "django", "python", "web", "python", "uv"]
tags_set = set(tags_list)

print("Множество:", tags_set)
print("Принадлежит ли \"uv\" множеству?", "uv" in tags_set)
print("Принадлежит ли \"fastapi\" множеству?", "fastapi" in tags_set)

tags_set.add("fastapi")
print("Обновленное множество:", tags_set)

tags_set.discard("rest api")
try:
    tags_set.remove("rest api")
except KeyError:
    pass

# Разница между discard и remove в том, что remove вызывает исключение при удалении несуществующего элемента
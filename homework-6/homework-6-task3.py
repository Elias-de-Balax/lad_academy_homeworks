"""3. Dict comprehension + Counter. Для списка слов words: постройте словарь {слово: длина} через dict comprehension;
    посчитайте частоту встречаемости слов через Counter; выведите топ-3 самых частых слова через most_common(3)."""
from collections import Counter

words_list = ["uv", "python", "django", "python", "web", "python", "uv"]
words_dict = {word: len(word) for word in words_list}
words_counter = Counter(words_list)

print("Словарь:", words_dict)
print("Частота слов:", dict(words_counter))
print("Топ-3 слов:", words_counter.most_common(3))
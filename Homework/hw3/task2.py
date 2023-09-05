import re
from collections import Counter
import requests
from bs4 import BeautifulSoup


def count_words(text):
    """
    Функция count_words принимает текст и выполняет следующие действия:
   - Удаляет знаки препинания и приводит текст к нижнему регистру с помощью регулярных выражений.
   - Разбивает текст на слова.
   - Подсчитывает количество встречаемых слов с помощью Counter.
   - Возвращает 10 самых частых слов в виде списка кортежей.
    """
    # Удаляем знаки препинания и приводим текст к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Разбиваем текст на слова
    words = text.split()

    # Подсчитываем количество встречаемых слов
    word_counts = Counter(words)

    # Возвращаем 10 самых частых слов
    return word_counts.most_common(10)


def get_text_from_url(url):
    response = requests.get(url)
    return response.text


def parse_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text


url = "https://docs.python.org/3.11/library/urllib.request.html?highlight=request#module-urllib.request"
html = get_text_from_url(url)
text = parse_text(html)

most_common_words = count_words(text)
print(most_common_words)

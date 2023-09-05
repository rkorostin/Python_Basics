import re
from collections import Counter
import requests
from bs4 import BeautifulSoup


def count_words(text):
    """
    Функция count_words принимает текст и производит подсчет слов,
    которые имеют более 3-х символов
    """
    # Удаляем знаки препинания и приводим текст к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Возвращаем список слов, удовлетворяющих регулярному выражению
    words = re.findall(r'\b\w+\b', text)

    #Подсчитываем количество слов, которые имеют длину больше 3-х символов.
    words = [word for word in words if len(word) > 3]

    # Подсчитываем количество встречаемых слов
    word_counts = Counter(words)

    # Возвращаем 10 самых частых слов
    return word_counts.most_common(10)


def get_text_from_url(url):
    """
    Функция get_text_from_url принимает URL-адрес и возвращает ответ в виде текста HTML.
    """
    response = requests.get(url)
    return response.text


def parse_text(html):
    """
    Функция parse_text принимает текст HTML, парсит его и возвращает текст
    """
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text


url = "https://docs.python.org/3.11/library/urllib.request.html?highlight=request#module-urllib.request"
html = get_text_from_url(url)
text = parse_text(html)

most_common_words = count_words(text)
print(most_common_words)

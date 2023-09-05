import requests  # для отправки HTTP-запросов
from bs4 import BeautifulSoup  # для парсинга HTML
from collections import Counter  # для подсчета количества элементов в списке
import re  # для работы с регулярными выражениями


def get_text_from_url(url):
    """
    Функция для получения текста с веб-страницы по заданному URL-адресу
    """
    response = requests.get(url)  # Отправляем GET-запрос по указанному URL-адресу
    soup = BeautifulSoup(response.content,
                         'html.parser')  # Создаем объект BeautifulSoup для парсинга HTML-кода страницы
    text_url = soup.get_text()  # Получаем текст со страницы
    return text_url


def parse_text(html_text):
    """
    Функция для обработки текста: удаление символов и приведение к нижнему регистру
    """
    html_text = re.sub(r'\W+', ' ', html_text)  # Удаляем все символы кроме букв и цифр
    html_text = html_text.lower()  # Приводим все символы к нижнему регистру
    return html_text


def count_words(text, max_word_length):
    """
    Функция для подсчета наиболее часто встречающихся слов в тексте
    """
    words = text.split()  # Разбиваем текст на слова
    filtered_words = [word for word in words if
                      len(word) > max_word_length]  # Оставляем слова, длина которых больше заданного значения
    word_counts = Counter(filtered_words)  # Подсчитываем количество каждого слова
    most_popular_words = word_counts.most_common(10)  # Получаем 10 наиболее часто встречающихся слов
    return most_popular_words


url = input("Введите URL-адрес: ")
max_word_length = int(input("Введите максимальное количество символов в слове: "))

html = get_text_from_url(url)  # Получаем HTML-текст по указанному URL-адресу
text = parse_text(html)  # Обрабатываем полученный текст
popular_words = count_words(text, max_word_length)  # Подсчитываем наиболее часто встречающиеся слова

print(popular_words)

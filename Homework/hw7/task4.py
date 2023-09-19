import random
import string
from pathlib import Path


def create_files(extension, min_name_length=6, max_name_length=30, min_bytes=256, max_bytes=4096, num_files=42):
    """
    Функция принимает параметры:
    extension - расширение файла
    min_name_length и max_name_length - минимальная и максимальная длины случайно сгенерированного имени файла
    min_bytes и max_bytes - минимальное и максимальное количество случайных байт
    num_files - количество файлов.
    """
    # Создаем директорию для файлов, если она не существует
    Path("files").mkdir(parents=True, exist_ok=True)

    # Генерируем указанное количество файлов
    for i in range(num_files):
        # Генерируем случайное имя файла:
        # выбираем случайные символы из заданного набора символов (строчные буквы и цифры)
        file_name = ''.join(
            random.choices(string.ascii_lowercase + string.digits, k=random.randint(min_name_length, max_name_length)))
        # Добавляем расширение к имени файла
        file_name += "." + extension

        # Генерируем случайное количество байт для файла
        num_bytes = random.randint(min_bytes, max_bytes)
        # Генерируем случайные байты через генератор списков
        file_data = bytes([random.randint(0, 255) for _ in range(num_bytes)])

        # Записываем данные в файл. Оператор / используем для объединения
        with open(Path("files") / file_name, "wb") as file:
            file.write(file_data)


# Пример
create_files("txt")

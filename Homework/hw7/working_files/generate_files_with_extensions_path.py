import random
import string
from pathlib import Path


def generate_files_with_extensions_path(extensions, num_files_per_extension, directory):
    """
    Функция генерирует файлы с заданными расширениями в указанной директории.
    Количество файлов для каждого расширения задается списком num_files_per_extension,
    а расширения - списком extensions. Файлы создаются со случайными именами от 1 до 7 символов.
    """
    # Создание директории, если она не существует
    Path(directory).mkdir(parents=True, exist_ok=True)

    # Генерация файлов для каждого расширения
    for extension, num_files in zip(extensions, num_files_per_extension):
        # Генерация заданного количества файлов с заданным расширением
        for i in range(num_files):
            # Генерация случайного имени файла
            file_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 7)))
            # Формирование пути к файлу с заданным именем и расширением
            file_path = Path(directory) / (file_name + "." + extension)
            # Создание файла по указанному пути
            file_path.touch()

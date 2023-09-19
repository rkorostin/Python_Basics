import shutil
from pathlib import Path


def sort_files(directory):
    """
    Функция выполняет сортировку файлов в заданной директории по группам:
     - видео
     - изображения
     - текстовые файлы
    """
    # Создаем директории для каждой группы файлов
    groups = ['video', 'image', 'text']
    for group in groups:
        group_dir = Path(directory) / group
        group_dir.mkdir(parents=True, exist_ok=True)

    # Получаем список всех файлов в исходной папке
    files = Path(directory).iterdir()

    # Сортируем файлы по группам
    for file in files:
        if file.is_file():
            # Определяем тип файла по расширению
            file_extension = file.suffix[1:]
            if file_extension in ['mp4', 'avi', 'mov']:
                # Перемещаем видео файлы в папку "video"
                destination = Path(directory) / 'video' / file.name
                shutil.move(str(file), str(destination))
            elif file_extension in ['jpg', 'png', 'gif']:
                # Перемещаем изображения в папку "image"
                destination = Path(directory) / 'image' / file.name
                shutil.move(str(file), str(destination))
            elif file_extension in ['txt', 'doc', 'pdf']:
                # Перемещаем текстовые файлы в папку "text"
                destination = Path(directory) / 'text' / file.name
                shutil.move(str(file), str(destination))

    # Удаляем оставшиеся файлы в исходной папке
    for file in Path(directory).iterdir():
        if file.is_file():
            file.unlink()

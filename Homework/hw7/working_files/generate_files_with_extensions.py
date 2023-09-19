from .create_files import create_files


def generate_files_with_extensions(extensions, num_files_per_extension):
    """
    Функция выполняет операции по созданию файлов с заданными расширениями и количеством файлов.
    Она принимает два аргумента:
     - "extensions" (список расширений файлов)
     - "num_files_per_extension" (список, содержащий количество файлов для каждого расширения).
    """
    # Проходим по каждому элементу в списках extensions и num_files_per_extension одновременно
    for extension, num_files in zip(extensions, num_files_per_extension):
        # Вызываем функцию create_files, передавая текущее расширение и количество файлов
        create_files(extension, num_files=num_files)

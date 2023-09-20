import os
import json
import csv
import pickle

def traverse_directory(directory: object) -> object:
    """
    Функция принимает на вход путь к директории и рекурсивно обходит ее.
    Результаты обхода сохраняются в два списка:
     - file_info - для файлов;
     - directory_info - для директорий;
    """
    # Проверяем существование директории
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Проверяем что директория это директория, а не что-то другое
    if not os.path.isdir(directory):
        print(f"'{directory}' is not a directory.")
        return

    # Создаем пустые списки для хранения результатов обхода
    file_info = []
    directory_info = []

    # Рекурсивно обходим директорию и все вложенные директории
    for root, dirs, files in os.walk(directory):
        # Для каждого файла получаем его полный путь (file_path) и размер в байтах (file_size).
        # Затем создаем словарь с информацией о файле и добавляем его в список file_info.
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_info.append({
                'path': file_path,
                'type': 'file',
                'size': file_size,
                'parent_directory': root
            })

        # Аналогично для каждой директории получаем ее полный путь (dir_path) и размер (dir_size),
        # который вычисляется с помощью функции get_directory_size.
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_directory_size(dir_path)
            directory_info.append({
                'path': dir_path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': root
            })

    # Сохраняем результаты обхода в файлы json, csv и pickle
    save_as_json(file_info, 'file_info.json')
    save_as_csv(file_info, 'file_info.csv')
    save_as_pickle(file_info, 'file_info.pickle')

    save_as_json(directory_info, 'directory_info.json')
    save_as_csv(directory_info, 'directory_info.csv')
    save_as_pickle(directory_info, 'directory_info.pickle')


def get_directory_size(directory):
    """
    Функция вычисляет общий размер всех файлов в указанной директории и ее поддиректориях.
    Возвращает общий размер в байтах.
    Для обхода всех файлов и подсчета их размеров используется функция os.path.getsize().
    """
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

def save_as_json(data, filename):
    """
    Функция сохраняет переданные данные в формате JSON в указанный файл.
    Она открывает файл для записи с помощью open() и использует функцию json.dump()
    для сериализации данных и записи их в файл.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def save_as_csv(data, filename):
    """
    Функция сохраняет переданные данные в формате CSV в указанный файл.
    Она открывает файл для записи с помощью open() и создает объект csv.DictWriter,
    который позволяет записывать данные в формате словаря в CSV-файл.
    Затем она записывает заголовок с помощью writer.writeheader() и все строки
    данных с помощью writer.writerows().
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_as_pickle(data, filename):
    """
    Функция сохраняет переданные данные в формате pickle в указанный файл.
    Она открывает файл для записи в двоичном режиме с помощью open() и использует
    функцию pickle.dump() для сериализации данных и записи их в файл.
    """
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Пример использования функции
traverse_directory("demo_folder")
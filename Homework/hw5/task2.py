def split_path(file_path):
    # Разделяем путь на директории и имя файла
    parts = file_path.split("/")
    path = "/".join(parts[:-1])
    filename = parts[-1]

    # Разделяем имя файла и расширение
    name_parts = filename.split(".")
    name = ".".join(name_parts[:-1])
    extension = "." + name_parts[-1]

    return path, name, extension


file_path = "/home/user/desktop/folder/example.txt"
path, name, extension = split_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)

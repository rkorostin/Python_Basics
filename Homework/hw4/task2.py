def create_reverse_dict(**kwargs):
    """
    Функция create_reverse_dict принимает произвольное количество именованных аргументов
    создает обратный словарь, в котором ключами являются значения аргументов,
    а значениями - имена аргументов
    """
    reverse_dict = {}

    print("Исходные параметры:")
    for key, value in kwargs.items():  # итерируемся по всем элементам через items()
        print(f"{key}: {value}")
        if isinstance(value, (list, dict, set)):  # проверка типа значения value на изменяемые объекты
            reverse_dict[str(value)] = key
        else:
            reverse_dict[str(value)] = key
    return reverse_dict


result = create_reverse_dict(int=1, float=5.5, str="hello",
                             list=[1, 2, 3], dict={"key": "value"},
                             set={1, 2, 3}, bool=True)
print("Обратный словарь: ", result)

# Словарь вещей, где ключ = предмет, значение = вес
dict_items = {
    'спальник': 3.7,
    'палатка': 4.2,
    'топор': 2.2,
    'нож': 1.3,
    'посуда': 3.3,
    'еда': 2.5,
    'вода': 2.9,
    'карта': 0.2,
    'компас': 0.3,
    'фонарик': 0.4,
    'зажигалка': 0.1
}


def fill_backpack(items, max_weight):
    """
    Функция fill_backpack принимает словарь и максимальный вес.
    Возвращает список предметов, которые помещаются в рюкзак с учетом ограничения на вес.
    """
    backpack = []
    current_weight = 0
    for item, weight in items.items():
        if current_weight + weight <= max_weight:
            backpack.append(item)
            current_weight += weight
    return backpack


def fill_backpack_all(items, max_weight):
    """
    Функция позволяет получить все возможные варианты сборки рюкзака из вещей items
    с ограничением по весу max_weight
    """
    backpacks = [[]]  # список для хранения всех возможных вариантов комплектации рюкзака
    for item, weight in items.items():  # итерация по каждому предмету и его весу из списка items.items()
        if weight <= max_weight:
            new_backpacks = []  # в новом списке будут храниться новые варианты сборки рюкзака
            for backpack in backpacks:  # итерируемся по каждому рюкзаку в списке backpacks.
                new_backpack = backpack + [item]  # создается новый рюкзак, который является
                # копией текущего рюкзака backpack, но с добавлением текущего предмета item
                new_backpacks.append(new_backpack)
            backpacks.extend(new_backpacks)
    return backpacks


max_weight = float(input("Введите максимальный вес рюкзака: "))

result = fill_backpack(dict_items, max_weight)
print("Максимальная вместимость рюкзака: ", result)
print()

choice = input("Хотите вывести список всех возможных вариантов сборки рюкзака? y/n: ")
while choice != 'y' and choice != 'n':
    choice = input("Некорректный ввод. Введите y или n: ")

if choice == 'y':
    result_all = fill_backpack_all(dict_items, max_weight)
    print("Все варианты сборки рюкзака: ")
    for i, backpack in enumerate(result_all):
        print(f"Вариант {i + 1}: {backpack}")

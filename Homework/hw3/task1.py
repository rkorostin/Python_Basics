import random


def find_duplicates(lst):
    result = []
    for i in lst:
        # Проверяем количество повторений элемента i в списке lst и добавляем его в список result,
        # если количество больше 1.
        if lst.count(i) > 1 and i not in result:
            result.append(i)
    return result


lst = [random.randint(1, 10) for _ in range(10)]
print("Дан список: ", lst)
print("Список дубликатов: ", find_duplicates(lst))

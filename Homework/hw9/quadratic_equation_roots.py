# -*- coding: utf-8 -*-
import csv
import json
import random


def csv_generator(filename, num_rows):
    """
    Функция отвечает за генерацию csv файла с тремя случайными числами в каждой строке.
    Имя файла csv и заданное количество строк задаём самостоятельно.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(row)


def decorator_quadratic_equation_roots(func):
    """
    Декоратор, который принимает функцию в качестве аргумента и возвращает
    обертку для этой функции в виде вывода в консоль квадратных уравнений и их корни, а
    также сохраняет результаты в json
    """
    def wrapper():
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            results = []
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                results.append({'a': a, 'b': b, 'c': c, 'result': result})
                print(f"Корни уравнения {a}x^2 + {b}x + {c}: {result}")

        with open('data.json', 'w') as file:
            json.dump(results, file)

    return wrapper


@decorator_quadratic_equation_roots
def quadratic_equation_roots(a, b, c):
    """
    Решение квадратного уравнения
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        roots = [root1, root2]
    elif discriminant == 0:
        root = -b / (2 * a)
        roots = [root]
    else:
        roots = []

    return roots


csv_generator('data.csv', random.randint(100, 1001))
quadratic_equation_roots()

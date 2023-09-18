from chess_package import random_queens
from chess_package import check_queens

# Создаем пустой список, в который будут добавляться корректные комбинации ферзей
queens_list_valid = []

while len(queens_list_valid) < 4:  # Выполняем цикл, пока не наберётся 4 списка с валидными координатами ферзей
    queens = random_queens()  # Генерируем случайную комбинацию ферзей
    result = check_queens(queens)  # Проверяем валидность комбинации ферзей
    if result:  # Если валидна, то добавляем комбинацию в список queens_list_valid
        queens_list_valid.append(queens)

for queens in queens_list_valid:
    print(queens)

"""
[(6, 4), (4, 3), (2, 2), (8, 1), (8, 1), (2, 2), (4, 3), (7, 8)]
[(6, 8), (7, 6), (5, 1), (4, 5), (2, 2), (7, 6), (3, 7), (3, 7)]
[(3, 8), (3, 8), (3, 8), (6, 4), (8, 5), (1, 2), (1, 2), (3, 8)]
[(8, 5), (6, 4), (2, 2), (3, 6), (6, 4), (1, 7), (3, 6), (3, 6)]
"""

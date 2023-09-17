from chess_package.random_queens import random_queens
from chess_package.check_queens import check_queens

# Создаем пустой список, в который будут добавляться корректные комбинации ферзей
queens_list_valid = []

while len(queens_list_valid) < 4:  # Выполняем цикл, пока не наберётся 4 списка с валидными координатами ферзей
    queens = random_queens()  # Генерируем случайную комбинацию ферзей
    result = check_queens(queens)  # Проверяем валидность комбинации ферзей
    if result:  # Если валидна, то добавляем комбинацию в список queens_list_valid
        queens_list_valid.append(queens)

for queens in queens_list_valid:
    print(queens)

from chess_package import check_queens

# queens = [(1, 1), (2, 7), (3, 5), (4, 8), (5, 2), (6, 4), (7, 6), (8, 3)]  # True
queens = [(1, 1), (2, 7), (3, 5), (4, 8), (5, 2), (6, 4), (7, 6), (8, 1)]  # False
result = check_queens(queens)
print(result)

def transpose_matrix(matrix):
    # Создаем пустую матрицу для хранения транспонированной матрицы
    transposed_matrix = []

    # Выводим исходную матрицу
    print("Исходная матрица:")
    for row in matrix:
        print(row)

    # Используем циклы for для прохода по столбцам и строкам исходной матрицы
    for i in range(len(matrix[0])):
        # Создаем пустую строку для текущего столбца транспонированной матрицы
        transposed_row = []

        for j in range(len(matrix)):
            # Добавляем элемент из текущего столбца исходной матрицы в текущую строку транспонированной матрицы
            transposed_row.append(matrix[j][i])

        # Добавляем текущую строку транспонированной матрицы в общую матрицу
        transposed_matrix.append(transposed_row)

    # Выводим транспонированную матрицу
    print("Транспонированная матрица:")
    for row in transposed_matrix:
        print(row)


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]]

transpose_matrix(matrix)

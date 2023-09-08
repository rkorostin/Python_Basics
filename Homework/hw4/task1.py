def transpose_matrix(matrix):
    transposed_matrix = []

    for i in range(len(matrix[0])):

        transposed_row = []

        for j in range(len(matrix)):
            transposed_row.append(matrix[j][i])

        transposed_matrix.append(transposed_row)

    for row in transposed_matrix:
        print(row)


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 8, 7, 6],
          [5, 4, 3, 2]]

transpose_matrix(matrix)

print("Таблица умножения".center(100) + "\n")

table = ((f"{i} x{j:2} = {i * j:2} " for i in range(2, 10)) for j in range(2, 11))
for row in table:
    print(*row)

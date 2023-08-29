# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним

a = input("Введите длину стороны a: ")
b = input("Введите длину стороны b: ")
c = input("Введите длину стороны c: ")

# проверяем, что пользователь ввел числа
try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    print("Ошибка: введите число")
else:
    # проверяем условие существования треугольника
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")

        # определяем тип треугольника
        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольник не существует")
# Для запроса ввода числа
def input_numbers(input_text):
    is_ok = False
    while not is_ok:
        try:
            number = float(input(input_text))
            is_ok = True
        except ValueError:
            print("Ошибка: введите число")
    return number

# Для проверки существования и определения типа треугольника
def check_triangle(a, b, c):
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


a = input_numbers("Введите длину стороны a: ")
b = input_numbers("Введите длину стороны b: ")
c = input_numbers("Введите длину стороны c: ")

check_triangle(a, b, c)
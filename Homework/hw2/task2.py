"""
Функция gcd(a, b) вычисляет наибольший общий делитель (НОД) двух чисел a и b
Пока b не равно нулю:
    - вычисляется значение остатка от деления a на b
    - a получает значение
    - b получает значение остатка от деления a на b
Когда b станет равно нулю - вернется значение a, которое будет являться наибольшим общим делителем a и b.
"""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


"""
Функция simplify_fraction(numerator, denominator) упрощает дробь:
1. Вычисляет наибольший общий делитель числителя и знаменателя с помощью функции gcd.
2. Делит числитель и знаменатель на найденный наибольший общий делитель.
3. Возвращает упрощенную дробь в виде кортежа (numerator, denominator).
"""
def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    return numerator, denominator  # было на семинаре, что так можно записывать


fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

# Разделяем числитель и знаменатель первой дроби
numerator1, denominator1 = fraction1.split('/')
numerator1 = int(numerator1)
denominator1 = int(denominator1)

# Разделяем числитель и знаменатель второй дроби
numerator2, denominator2 = fraction2.split('/')
numerator2 = int(numerator2)
denominator2 = int(denominator2)

# Вычисляем сумму дробей
sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
sum_denominator = denominator1 * denominator2

# Вычисляем произведение дробей
product_numerator = numerator1 * numerator2
product_denominator = denominator1 * denominator2

# Упрощаем результаты
sum_numerator, sum_denominator = simplify_fraction(sum_numerator, sum_denominator)
product_numerator, product_denominator = simplify_fraction(product_numerator, product_denominator)

# Добавляем проверку, что если числитель равен знаменателю, то выводить целое число 1
# Проверка нулевого знаменателя
if sum_denominator == 0:
    print("Сумма дробей: Ошибка (деление на 0)")
else:
    if sum_numerator == sum_denominator:
        print("Сумма дробей: 1")
    else:
        print("Сумма дробей:", f"{sum_numerator}/{sum_denominator}")

if product_denominator == 0:
    print("Произведение дробей: Ошибка (деление на 0)")
else:
    if product_numerator == product_denominator:
        print("Произведение дробей: 1")
    else:
        print("Произведение дробей:", f"{product_numerator}/{product_denominator}")

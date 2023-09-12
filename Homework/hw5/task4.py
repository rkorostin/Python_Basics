def fibonacci_generator():
    """
    Бесконечный генератор чисел Фибоначчи
    """
    a, b = 0, 1  # переменные a и b хранят текущее и предыдущее числа Фибоначчи
    while True:
        yield a  # возвращаем текущее число Фибоначчи - a
        a, b = b, a + b  # обновляем значения переменных a и b


fib = fibonacci_generator()
print(next(fib))  # Вывод: 0
print(next(fib))  # Вывод: 1
print(next(fib))  # Вывод: 1
print(next(fib))  # Вывод: 2
print(next(fib))  # Вывод: 3
print(next(fib))  # Вывод: 5
print(next(fib))  # Вывод: 8

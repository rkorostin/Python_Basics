def prime_generator(n):
    """
    Функция генерирует N простых чисел, начиная с числа 2
    """
    count = 0
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Если число делится нацело на какое-либо число от 2
            # до квадратного корня из самого числа, то оно не является простым
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num  # простое число передаём оператору yield
            count += 1

        num += 1

n = int(input("Сколько сгенерировать простых чисел (начиная с 2)?: "))

for prime in prime_generator(n):
    print(prime)
